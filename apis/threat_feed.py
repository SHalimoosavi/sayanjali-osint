from threat_feeds.reputation_db import (
    KNOWN_MALICIOUS_IPS,
    KNOWN_MALICIOUS_DOMAINS,
    KNOWN_MALICIOUS_EMAILS,
    KNOWN_MALICIOUS_URLS
)


def correlate_threat_feeds(report: dict) -> dict:

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

    malicious_ips = [
        ip for ip in ips
        if ip in KNOWN_MALICIOUS_IPS
    ]

    malicious_domains = [
        domain for domain in domains
        if domain.lower() in KNOWN_MALICIOUS_DOMAINS
    ]

    malicious_emails = [
        email for email in emails
        if email.lower() in KNOWN_MALICIOUS_EMAILS
    ]

    malicious_urls = [
        url for url in urls
        if url in KNOWN_MALICIOUS_URLS
    ]

    threat_score = (
        len(malicious_ips) * 25
        + len(malicious_domains) * 25
        + len(malicious_emails) * 20
        + len(malicious_urls) * 20
    )

    threat_score = min(
        threat_score,
        100
    )

    if threat_score == 0:
        verdict = "Low Risk"

    elif threat_score <= 40:
        verdict = "Medium Risk"

    elif threat_score <= 75:
        verdict = "High Risk"

    else:
        verdict = "Critical Risk"

    return {
        "malicious_ips": malicious_ips,
        "malicious_domains": malicious_domains,
        "malicious_emails": malicious_emails,
        "malicious_urls": malicious_urls,
        "threat_score": threat_score,
        "verdict": verdict
    }
