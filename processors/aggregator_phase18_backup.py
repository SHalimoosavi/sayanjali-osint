import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from cache.cache_manager import CacheManager

from validators import detect_query_type, resolve_domain_to_ip

from apis.ioc_risk import calculate_ioc_risk
from apis.threat_feed import correlate_threat_feeds

from apis.ssl_intelligence import ssl_intelligence

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
    radius: int = 500,
    deep: bool = False
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

        # ==================================================
        # IP INVESTIGATION
        # ==================================================

        if q_type == "ip":

            ip_data = await lookup_ip(norm_query)

            report["ip_geolocation"] = ip_data

            with ThreadPoolExecutor(max_workers=6) as executor:

                reverse_dns_future = executor.submit(
                    reverse_dns_lookup,
                    norm_query
                )

                asn_future = executor.submit(
                    lookup_asn,
                    norm_query
                )

                vt_future = executor.submit(
                    lookup_virustotal,
                    norm_query,
                    "ip"
                )

                shodan_future = executor.submit(
                    lookup_shodan,
                    norm_query
                )

                abuse_future = executor.submit(
                    lookup_abuseipdb,
                    norm_query
                )

                otx_future = executor.submit(
                    lookup_otx,
                    norm_query,
                    "ip"
                )

                report["reverse_dns"] = reverse_dns_future.result()
                report["asn_info"] = asn_future.result()
                report["virustotal"] = vt_future.result()
                report["shodan"] = shodan_future.result()
                report["abuseipdb"] = abuse_future.result()
                report["otx"] = otx_future.result()

            report["latitude"] = ip_data.get("latitude")
            report["longitude"] = ip_data.get("longitude")

            sources.extend([
                "ip_geolocation",
                "reverse_dns",
                "asn_lookup",
                "virustotal",
                "shodan",
                "abuseipdb",
                "otx"
            ])

        # ==================================================
        # DOMAIN INVESTIGATION
        # ==================================================

        elif q_type == "domain":

            ip = resolve_domain_to_ip(norm_query)

            report["domain_info"] = {
                "domain": norm_query,
                "primary_ip": ip,
                "all_ips": [ip]
            }

            with ThreadPoolExecutor(max_workers=9) as executor:

                whois_future = executor.submit(
                    lookup_whois,
                    norm_query
                )

                dns_future = executor.submit(
                    get_dns_records,
                    norm_query
                )

                subdomains_future = executor.submit(
                    enumerate_subdomains,
                    norm_query
                )

                reverse_dns_future = executor.submit(
                    reverse_dns_lookup,
                    ip
                )

                asn_future = executor.submit(
                    lookup_asn,
                    ip
                )

                vt_future = executor.submit(
                    lookup_virustotal,
                    norm_query,
                    "domain"
                )

                shodan_future = executor.submit(
                    lookup_shodan,
                    ip
                )

                abuse_future = executor.submit(
                    lookup_abuseipdb,
                    ip
                )

                otx_future = executor.submit(
                    lookup_otx,
                    norm_query,
                    "domain"
                )

                report["whois"] = whois_future.result()
                report["dns_records"] = dns_future.result()
                report["subdomains"] = subdomains_future.result()
                report["reverse_dns"] = reverse_dns_future.result()
                report["asn_info"] = asn_future.result()
                report["virustotal"] = vt_future.result()
                report["shodan"] = shodan_future.result()
                report["abuseipdb"] = abuse_future.result()
                report["otx"] = otx_future.result()

            ip_data = await lookup_ip(ip)

            report["ip_geolocation"] = ip_data

            report["latitude"] = ip_data.get("latitude")
            report["longitude"] = ip_data.get("longitude")

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

        # ==================================================
        # COORDINATES
        # ==================================================

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

        # ==================================================
        # ADDRESS
        # ==================================================

        elif q_type == "address":

            report["forward_geocode"] = await forward_geocode(
                norm_query
            )

            if report["forward_geocode"]:

                report["latitude"] = (
                    report["forward_geocode"].get("latitude")
                )

                report["longitude"] = (
                    report["forward_geocode"].get("longitude")
                )

            sources.append(
                "forward_geocoding"
            )

        # ==================================================
        # NEARBY SEARCH
        # ==================================================

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

        # ==================================================
        # IOC EXTRACTION
        # ==================================================

        ioc_text = ""

        for key in report:
            try:
                ioc_text += str(report[key]) + " "
            except Exception:
                pass

        report["ioc_summary"] = extract_iocs(
            ioc_text
        )

        # ==================================================
        # EMAIL INTELLIGENCE
        # ==================================================

        report["email_intelligence"] = (
            analyze_email_intelligence(report)
        )

        sources.append(
            "email_intelligence"
        )

        # ==================================================
        # USERNAME INTELLIGENCE
        # ==================================================

        username_target = None

        if q_type == "domain":
            username_target = norm_query.split(".")[0]

        elif q_type == "address":
            username_target = norm_query.replace(
                " ",
                ""
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

        # ==================================================
        # IOC RISK
        # ==================================================

        report["ioc_risk"] = calculate_ioc_risk(
            report
        )

        sources.append(
            "ioc_risk"
        )

        # ==================================================
        # THREAT FEED
        # ==================================================

        report["threat_feed"] = correlate_threat_feeds(
            report
        )

        sources.append(
            "threat_feed"
        )

        # ==================================================
        # AI SUMMARY
        # ==================================================

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
