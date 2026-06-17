import re


def analyze_email_intelligence(report: dict) -> dict:

    emails = []

    ioc_summary = report.get(
        "ioc_summary",
        {}
    )

    emails.extend(
        ioc_summary.get(
            "emails",
            []
        )
    )

    dns_records = report.get(
        "dns_records",
        {}
    )

    txt_records = dns_records.get(
        "TXT",
        []
    )

    spf_detected = False
    dmarc_detected = False

    for record in txt_records:

        lower = record.lower()

        if "v=spf1" in lower:
            spf_detected = True

        if "dmarc" in lower:
            dmarc_detected = True

    domains = []

    for email in emails:

        try:

            domains.append(
                email.split("@")[1]
            )

        except Exception:
            pass

    domains = sorted(
        list(
            set(domains)
        )
    )

    return {
        "emails_found": len(emails),
        "emails": emails,
        "email_domains": domains,
        "spf_detected": spf_detected,
        "dmarc_detected": dmarc_detected
    }
