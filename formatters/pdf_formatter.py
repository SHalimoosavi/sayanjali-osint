from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report: dict, output_path: str):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "SAYANJALI OSINT REPORT",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            f"Query: {report.get('query', 'N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Query Type: {report.get('query_type', 'N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated: {report.get('timestamp', 'N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    if report.get("ai_summary"):

        ai = report["ai_summary"]

        elements.append(
            Paragraph(
                "Executive Summary",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Risk Score: {ai.get('risk_score', 'N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Verdict: {ai.get('verdict', 'N/A')}",
                styles["Normal"]
            )
        )

        findings = ai.get(
            "findings",
            []
        )

        for item in findings:

            elements.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

    elements.append(
        PageBreak()
    )

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
                f"Domain: {domain.get('domain')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Primary IP: {domain.get('primary_ip')}",
                styles["Normal"]
            )
        )

    if report.get("whois"):

        whois = report["whois"]

        elements.append(
            Spacer(1, 10)
        )

        elements.append(
            Paragraph(
                "WHOIS Information",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Registrar: {whois.get('registrar')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Creation Date: {whois.get('creation_date')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Expiration Date: {whois.get('expiration_date')}",
                styles["Normal"]
            )
        )

    if report.get("reverse_dns"):

        rdns = report["reverse_dns"]

        if not rdns.get("error"):

            elements.append(
                Spacer(1, 10)
            )

            elements.append(
                Paragraph(
                    "Reverse DNS",
                    styles["Heading1"]
                )
            )

            elements.append(
                Paragraph(
                    f"Hostname: {rdns.get('hostname')}",
                    styles["Normal"]
                )
            )

    if report.get("asn_info"):

        asn = report["asn_info"]

        elements.append(
            Spacer(1, 10)
        )

        elements.append(
            Paragraph(
                "ASN Intelligence",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"ASN: {asn.get('asn')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Organization: {asn.get('organization')}",
                styles["Normal"]
            )
        )

    if report.get("virustotal"):

        vt = report["virustotal"]

        elements.append(
            Spacer(1, 10)
        )

        elements.append(
            Paragraph(
                "VirusTotal Intelligence",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                f"Reputation: {vt.get('reputation', 'N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Malicious: {vt.get('malicious', 'N/A')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Suspicious: {vt.get('suspicious', 'N/A')}",
                styles["Normal"]
            )
        )

    doc.build(elements)
