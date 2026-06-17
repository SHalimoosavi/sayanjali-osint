import time
from datetime import datetime

from cache.cache_manager import CacheManager

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
from apis.abuseipdb import lookup_abuseipdb
from apis.otx_lookup import lookup_otx

from apis.subdomain_enum import enumerate_subdomains
from apis.email_intelligence import analyze_email_intelligence
from apis.username_intelligence import username_lookup

from utils.ioc_extractor import extract_iocs


async def run_investigation(
    query: str,
    nearby_type: str = None,
    radius: int = 500
) -> dict:

    start_time = time.time()

    q_type, norm_query = detect_query_type(query)

    cache = CacheManager()

    cached = cache.get(query)

    if cached:
        cached["cache_status"] = "HIT"
        return cached

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

        # =====================================
        # IP INVESTIGATION
        # =====================================

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

            report["abuseipdb"] = lookup_abuseipdb(
                norm_query
            )

            report["otx"] = lookup_otx(
                norm_query,
                "ip"
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
                "shodan",
                "abuseipdb",
                "otx"
            ])

        # =====================================
        # DOMAIN INVESTIGATION
        # =====================================

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

            report["subdomains"] = enumerate_subdomains(
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

            report["abuseipdb"] = lookup_abuseipdb(
                ip
            )

            report["otx"] = lookup_otx(
                norm_query,
                "domain"
            )

            ip_data = await lookup_ip(
                ip
            )

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
                "subdomain_enum",
                "reverse_dns",
                "asn_lookup",
                "virustotal",
                "shodan",
                "abuseipdb",
                "otx",
                "ip_geolocation"
            ])

        # =====================================
        # COORDINATES
        # =====================================

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

        # =====================================
        # ADDRESS
        # =====================================

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

        # =====================================
        # NEARBY SEARCH
        # =====================================

        if nearby_type and report.get("latitude"):

            report["nearby_places"] = await search_places(
                report["latitude"],
                report["longitude"],
                nearby_type,
                radius
            )

            sources.append(
                "overpass_poi"
            )

        # =====================================
        # IOC EXTRACTION
        # =====================================

        ioc_text = ""

        for key in [
            "query",
            "domain_info",
            "whois",
            "dns_records",
            "subdomains",
            "reverse_dns",
            "shodan",
            "abuseipdb",
            "otx"
        ]:

            if report.get(key):
                ioc_text += str(report[key]) + " "

        report["ioc_summary"] = extract_iocs(
            ioc_text
        )

        # =====================================
        # EMAIL INTELLIGENCE
        # =====================================

        report["email_intelligence"] = (
            analyze_email_intelligence(
                report
            )
        )

        sources.append(
            "email_intelligence"
        )

        # =====================================
        # USERNAME INTELLIGENCE
        # =====================================

        username_target = None

        if q_type == "domain":

            username_target = (
                norm_query.split(".")[0]
            )

        elif q_type == "address":

            username_target = (
                norm_query.replace(
                    " ",
                    ""
                )
            )

        if username_target:

            report["username_intelligence"] = (
                username_lookup(
                    username_target
                )
            )

            sources.append(
                "username_intelligence"
            )

        # =====================================
        # THREAT CORRELATION
        # =====================================

        report["ai_summary"] = generate_ai_summary(
            report
        )

    except Exception as e:

        errors.append(
            str(e)
        )

    report["sources_queried"] = sources

    report["errors"] = errors

    report["processing_time_seconds"] = round(
        time.time() - start_time,
        2
    )

    report["confidence_score"] = (
        0.8 if not errors else 0.5
    )

    report["cache_status"] = "MISS"

    cache.set(
        query,
        report
    )

    return report
