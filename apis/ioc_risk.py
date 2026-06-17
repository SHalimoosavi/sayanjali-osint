def calculate_ioc_risk(report: dict) -> dict:

    iocs = report.get(
        "ioc_summary",
        {}
    )

    ips = iocs.get(
        "ips",
        []
    )

    domains = iocs.get(
        "domains",
        []
    )

    emails = iocs.get(
        "emails",
        []
    )

    urls = iocs.get(
        "urls",
        []
    )

    suspicious_ips = 0
    suspicious_domains = 0
    suspicious_emails = 0

    risk_score = 0

    abuse = report.get(
        "abuseipdb",
        {}
    )

    if abuse.get(
        "abuse_score",
        0
    ) >= 25:

        suspicious_ips += 1
        risk_score += 20

    vt = report.get(
        "virustotal",
        {}
    )

    if vt.get(
        "malicious",
        0
    ) > 0:

        suspicious_domains += 1
        risk_score += 30

    total_iocs = (
        len(ips)
        + len(domains)
        + len(emails)
        + len(urls)
    )

    risk_score += min(
        total_iocs,
        20
    )

    risk_score = min(
        risk_score,
        100
    )

    if risk_score <= 20:
        verdict = "Low Risk"

    elif risk_score <= 50:
        verdict = "Medium Risk"

    elif risk_score <= 75:
        verdict = "High Risk"

    else:
        verdict = "Critical Risk"

    return {
        "ioc_count": total_iocs,
        "suspicious_ips": suspicious_ips,
        "suspicious_domains": suspicious_domains,
        "suspicious_emails": suspicious_emails,
        "risk_score": risk_score,
        "verdict": verdict
    }
