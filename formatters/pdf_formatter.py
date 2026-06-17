from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf(
    report: dict,
    output_path: str
):

    doc = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    elements = []

    # ==================================================
    # COVER PAGE
    # ==================================================

    elements.append(
        Paragraph(
            "SAYANJALI OSINT",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "Executive Intelligence Report",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Target: {report.get('query','N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Type: {report.get('query_type','N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated: {report.get('timestamp','N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    ai = report.get(
        "ai_summary",
        {}
    )

    elements.append(
        Paragraph(
            f"Risk Score: {ai.get('risk_score','N/A')}",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Verdict: {ai.get('verdict','N/A')}",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Confidence: {ai.get('confidence','N/A')}",
            styles["Heading2"]
        )
    )

    elements.append(
        PageBreak()
    )

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    elements.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    findings = ai.get(
        "findings",
        []
    )

    if findings:

        for item in findings:

            elements.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No findings available",
                styles["Normal"]
            )
        )

    elements.append(
        PageBreak()
    )

    # ==================================================
    # DOMAIN
    # ==================================================

    if report.get("domain_info"):

        domain = report["domain_info"]

        elements.append(
            Paragraph(
                "Domain Information",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Domain: {domain.get('domain','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Primary IP: {domain.get('primary_ip','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    # ==================================================
    # ASN
    # ==================================================

    if report.get("asn_info"):

        asn = report["asn_info"]

        elements.append(
            Paragraph(
                "ASN Intelligence",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"ASN: {asn.get('asn','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Organization: {asn.get('organization','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Network: {asn.get('network','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Country: {asn.get('country','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    # ==================================================
    # VIRUSTOTAL
    # ==================================================

    if report.get("virustotal"):

        vt = report["virustotal"]

        elements.append(
            Paragraph(
                "VirusTotal Intelligence",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Reputation: {vt.get('reputation','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Harmless: {vt.get('harmless','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Malicious: {vt.get('malicious','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Suspicious: {vt.get('suspicious','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Undetected: {vt.get('undetected','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    # ==================================================
    # SHODAN
    # ==================================================

    if report.get("shodan"):

        shodan = report["shodan"]

        elements.append(
            Paragraph(
                "Shodan Intelligence",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Organization: {shodan.get('organization','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Country: {shodan.get('country','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Operating System: {shodan.get('os','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Ports: {', '.join(map(str, shodan.get('ports', [])))}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    # ==================================================
    # ABUSEIPDB
    # ==================================================

    if report.get("abuseipdb"):

        abuse = report["abuseipdb"]

        elements.append(
            Paragraph(
                "AbuseIPDB Intelligence",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Abuse Score: {abuse.get('abuse_score','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"ISP: {abuse.get('isp','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Domain: {abuse.get('domain','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Reports: {abuse.get('total_reports','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    # ==================================================
    # OTX
    # ==================================================

    if report.get("otx"):

        otx = report["otx"]

        elements.append(
            Paragraph(
                "AlienVault OTX Intelligence",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Indicator: {otx.get('indicator','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Type: {otx.get('indicator_type','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Reputation: {otx.get('reputation','N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Pulse Count: {otx.get('pulse_count','N/A')}",
                styles["Normal"]
            )
        )

    elements.append(
        PageBreak()
    )

    # ==================================================
    # METADATA
    # ==================================================

    elements.append(
        Paragraph(
            "Investigation Metadata",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"Processing Time: {report.get('processing_time_seconds')}s",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Cache Status: {report.get('cache_status','N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Confidence Score: {report.get('confidence_score','N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Sources Queried: {', '.join(report.get('sources_queried', []))}",
            styles["Normal"]
        )
    )

    if report.get("errors"):

        elements.append(
            Paragraph(
                f"Errors: {', '.join(report.get('errors', []))}",
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Generated by SAYANJALI OSINT v2.0",
            styles["Heading2"]
        )
    )

    doc.build(
        elements
    )
