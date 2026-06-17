from rich.console import Console
from rich.panel import Panel
from rich.table import Table


def format_cli(report: dict):

    console = Console()

    # ==================================================
    # HEADER
    # ==================================================

    console.print(
        Panel(
            f"[bold cyan]SAYANJALI OSINT Report[/bold cyan]\n"
            f"Query: [yellow]{report.get('query')}[/yellow]\n"
            f"Type: [green]{report.get('query_type')}[/green]\n"
            f"Time: {report.get('processing_time_seconds')}s",
            expand=False
        )
    )

    # ==================================================
    # CACHE
    # ==================================================

    if report.get("cache_status"):
        console.print(
            Panel(
                f"Cache Status: {report.get('cache_status')}",
                title="Cache",
                border_style="blue",
                expand=False
            )
        )

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    if report.get("ai_summary"):

        ai = report["ai_summary"]

        findings = "\n".join(
            f"• {x}" for x in ai.get("findings", [])
        )

        console.print(
            Panel(
                f"Risk Score: {ai.get('risk_score')}\n"
                f"Verdict: {ai.get('verdict')}\n"
                f"Confidence: {ai.get('confidence')}\n\n"
                f"{findings}",
                title="Executive Summary",
                border_style="green"
            )
        )

    # ==================================================
    # IOC RISK
    # ==================================================

    if report.get("ioc_risk"):

        ioc = report["ioc_risk"]

        table = Table(title="IOC Risk Assessment")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row(
            "IOC Count",
            str(ioc.get("ioc_count"))
        )

        table.add_row(
            "Suspicious IPs",
            str(ioc.get("suspicious_ips"))
        )

        table.add_row(
            "Suspicious Domains",
            str(ioc.get("suspicious_domains"))
        )

        table.add_row(
            "Suspicious Emails",
            str(ioc.get("suspicious_emails"))
        )

        table.add_row(
            "Risk Score",
            str(ioc.get("risk_score"))
        )

        table.add_row(
            "Verdict",
            str(ioc.get("verdict"))
        )

        console.print(table)

    # ==================================================
    # THREAT FEED
    # ==================================================

    if report.get("threat_feed"):

        threat = report["threat_feed"]

        table = Table(title="Threat Feed Correlation")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row(
            "Malicious IPs",
            str(len(threat.get("malicious_ips", [])))
        )

        table.add_row(
            "Malicious Domains",
            str(len(threat.get("malicious_domains", [])))
        )

        table.add_row(
            "Malicious Emails",
            str(len(threat.get("malicious_emails", [])))
        )

        table.add_row(
            "Malicious URLs",
            str(len(threat.get("malicious_urls", [])))
        )

        table.add_row(
            "Threat Score",
            str(threat.get("threat_score"))
        )

        table.add_row(
            "Verdict",
            str(threat.get("verdict"))
        )

        console.print(table)

    # ==================================================
    # ASN
    # ==================================================

    if report.get("asn_info"):

        asn = report["asn_info"]

        table = Table(title="ASN Intelligence")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row("ASN", str(asn.get("asn")))
        table.add_row("Organization", str(asn.get("organization")))
        table.add_row("Network", str(asn.get("network")))
        table.add_row("Country", str(asn.get("country")))

        console.print(table)

    # ==================================================
    # SHODAN
    # ==================================================

    if report.get("shodan"):

        shodan = report["shodan"]

        table = Table(title="Shodan Intelligence")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row("Organization", str(shodan.get("organization")))
        table.add_row("Country", str(shodan.get("country")))
        table.add_row("OS", str(shodan.get("os")))
        table.add_row(
            "Ports",
            ", ".join(map(str, shodan.get("ports", [])))
        )

        console.print(table)

    # ==================================================
    # VIRUSTOTAL
    # ==================================================

    if report.get("virustotal"):

        vt = report["virustotal"]

        table = Table(title="VirusTotal Intelligence")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row("Reputation", str(vt.get("reputation")))
        table.add_row("Malicious", str(vt.get("malicious")))
        table.add_row("Suspicious", str(vt.get("suspicious")))
        table.add_row("Harmless", str(vt.get("harmless")))

        console.print(table)

    # ==================================================
    # ABUSEIPDB
    # ==================================================

    if report.get("abuseipdb"):

        abuse = report["abuseipdb"]

        table = Table(title="AbuseIPDB Intelligence")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row(
            "Abuse Score",
            str(abuse.get("abuse_score"))
        )

        table.add_row(
            "Reports",
            str(abuse.get("total_reports"))
        )

        table.add_row(
            "ISP",
            str(abuse.get("isp"))
        )

        console.print(table)

    # ==================================================
    # OTX
    # ==================================================

    if report.get("otx"):

        otx = report["otx"]

        table = Table(title="AlienVault OTX Intelligence")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row(
            "Pulse Count",
            str(otx.get("pulse_count"))
        )

        table.add_row(
            "Reputation",
            str(otx.get("reputation"))
        )

        table.add_row(
            "ASN",
            str(otx.get("asn"))
        )

        console.print(table)

    # ==================================================
    # ERRORS
    # ==================================================

    if report.get("errors"):

        if len(report["errors"]) > 0:

            console.print(
                Panel(
                    "\n".join(report["errors"]),
                    title="Errors",
                    border_style="red"
                )
            )
