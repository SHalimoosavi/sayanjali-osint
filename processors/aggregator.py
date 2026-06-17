from datetime import datetime
import time

from cache.cache_manager import CacheManager

from validators import detect_query_type

from apis.ai_summary import generate_ai_summary
from apis.email_intelligence import analyze_email_intelligence
from apis.username_intelligence import username_lookup
from apis.ioc_risk import calculate_ioc_risk

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
        # IOC EXTRACTION
        # =====================================

        report["ioc_summary"] = extract_iocs(
            str(query)
        )

        # =====================================
        # IOC RISK ENGINE
        # =====================================

        report["ioc_risk"] = calculate_ioc_risk(
            report
        )

        sources.append(
            "ioc_risk"
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

        # =====================================
        # AI SUMMARY
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
