import time
from datetime import datetime

from validators import detect_query_type, resolve_domain_to_ip

from apis.ai_summary import generate_ai_summary
from apis.ip_geolocation import lookup_ip
from apis.nominatim import reverse_geocode, forward_geocode
from apis.overpass import search_places

from apis.whois_lookup import lookup_whois
from apis.dns_lookup import get_dns_records
from apis.reverse_dns import reverse_dns_lookup
from apis.asn_lookup import lookup_asn
from apis.virustotal import lookup_virustotal
from apis.shodan_lookup import lookup_shodan


async def run_investigation(
    query: str,
    nearby_type: str = None,
    radius: int = 500
) -> dict:

    start_time = time.time()

    q_type, norm_query = detect_query_type(query)

    report = {
        "query": query,
        "query_type": q_type,
        "timestamp": datetime.now().isoformat(),
        "sources_queried": [],
        "errors": []
    }

    sources = []
    errors = []

    try:

        if q_type == "ip":

            ip_data = await lookup_ip(norm_query)

            report["ip_geolocation"] = ip_data

            report["reverse_dns"] = reverse_dns_lookup(
                norm_query
            )

            report["asn_info"] = lookup_asn(
                norm_query
            )

            report["virustotal"] = lookup_virustotal(
                norm_query,
                "ip"
            )

            report["shodan"] = lookup_shodan(
                norm_query
            )

            report["latitude"] = ip_data.get(
                "latitude"
            )

            report["longitude"] = ip_data.get(
                "longitude"
            )

            sources.extend([
                "ip_geolocation",
                "reverse_dns",
                "asn_lookup",
                "virustotal",
                "shodan"
            ])

        elif q_type == "domain":

            ip = resolve_domain_to_ip(
                norm_query
            )

            report["domain_info"] = {
                "domain": norm_query,
                "primary_ip": ip,
                "all_ips": [ip]
            }

            report["whois"] = lookup_whois(
                norm_query
            )

            report["dns_records"] = get_dns_records(
                norm_query
            )

            report["reverse_dns"] = reverse_dns_lookup(
                ip
            )

            report["asn_info"] = lookup_asn(
                ip
            )

            report["virustotal"] = lookup_virustotal(
                norm_query,
                "domain"
            )

            report["shodan"] = lookup_shodan(
                ip
            )

            ip_data = await lookup_ip(ip)

            report["ip_geolocation"] = ip_data

            report["latitude"] = ip_data.get(
                "latitude"
            )

            report["longitude"] = ip_data.get(
                "longitude"
            )

            sources.extend([
                "whois",
                "dns",
                "reverse_dns",
                "asn_lookup",
                "virustotal",
                "shodan",
                "ip_geolocation"
            ])

        elif q_type == "coordinates":

            lat, lon = map(
                float,
                norm_query.split(",")
            )

            report["latitude"] = lat
            report["longitude"] = lon

            report["reverse_geocode"] = await reverse_geocode(
                lat,
                lon
            )

            sources.append(
                "reverse_geocoding"
            )

        elif q_type == "address":

            report["forward_geocode"] = await forward_geocode(
                norm_query
            )

            if report["forward_geocode"]:

                report["latitude"] = report[
                    "forward_geocode"
                ].get("latitude")

                report["longitude"] = report[
                    "forward_geocode"
                ].get("longitude")

            sources.append(
                "forward_geocoding"
            )

        if nearby_type and report.get(
            "latitude"
        ):

            report["nearby_places"] = await search_places(
                report["latitude"],
                report["longitude"],
                nearby_type,
                radius
            )

            sources.append(
                "overpass_poi"
            )

        report["ai_summary"] = generate_ai_summary(
            report
        )

    except Exception as e:

        errors.append(str(e))

    report["sources_queried"] = sources
    report["errors"] = errors

    report["processing_time_seconds"] = round(
        time.time() - start_time,
        2
    )

    report["confidence_score"] = (
        0.8 if not errors else 0.5
    )

    return report
