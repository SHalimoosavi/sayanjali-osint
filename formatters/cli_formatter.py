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
    # CACHE STATUS
    # ==================================================

    if report.get("cache_status"):

        console.print(
            Panel(
                f"[bold]Cache Status:[/bold] {report.get('cache_status')}",
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
                f"[bold]Risk Score:[/bold] {ai.get('risk_score')}\n"
                f"[bold]Verdict:[/bold] {ai.get('verdict')}\n"
                f"[bold]Confidence:[/bold] {ai.get('confidence', 'N/A')}\n\n"
                f"{findings}",
                title="Executive Summary",
                border_style="green"
            )
        )

    # ==================================================
    # DOMAIN INFO
    # ==================================================

    if report.get("domain_info"):

        domain = report["domain_info"]

        table = Table(title="Domain Information")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row(
            "Domain",
            str(domain.get("domain"))
        )

        table.add_row(
            "Primary IP",
            str(domain.get("primary_ip"))
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

        table.add_row(
            "ASN",
            str(asn.get("asn"))
        )

        table.add_row(
            "Organization",
            str(asn.get("organization"))
        )

        table.add_row(
            "Network",
            str(asn.get("network"))
        )

        table.add_row(
            "Country",
            str(asn.get("country"))
        )

        console.print(table)

    # ==================================================
    # SHODAN
    # ==================================================

    if report.get("shodan"):

        shodan = report["shodan"]

        table = Table(title="Shodan Intelligence")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row(
            "Organization",
            str(shodan.get("organization"))
        )

        table.add_row(
            "Country",
            str(shodan.get("country"))
        )

        table.add_row(
            "Operating System",
            str(shodan.get("os"))
        )

        table.add_row(
            "Hostnames",
            ", ".join(
                shodan.get("hostnames", [])
            )
        )

        table.add_row(
            "Ports",
            ", ".join(
                map(str, shodan.get("ports", []))
            )
        )

        table.add_row(
            "Last Update",
            str(shodan.get("last_update"))
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

        table.add_row(
            "Reputation",
            str(vt.get("reputation"))
        )

        table.add_row(
            "Harmless",
            str(vt.get("harmless"))
        )

        table.add_row(
            "Malicious",
            str(vt.get("malicious"))
        )

        table.add_row(
            "Suspicious",
            str(vt.get("suspicious"))
        )

        table.add_row(
            "Undetected",
            str(vt.get("undetected"))
        )

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
            "ISP",
            str(abuse.get("isp"))
        )

        table.add_row(
            "Domain",
            str(abuse.get("domain"))
        )

        table.add_row(
            "Usage Type",
            str(abuse.get("usage_type"))
        )

        table.add_row(
            "Total Reports",
            str(abuse.get("total_reports"))
        )

        table.add_row(
            "Last Reported",
            str(abuse.get("last_reported"))
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
            "Indicator",
            str(otx.get("indicator"))
        )

        table.add_row(
            "Type",
            str(otx.get("indicator_type"))
        )

        table.add_row(
            "Reputation",
            str(otx.get("reputation"))
        )

        table.add_row(
            "Pulse Count",
            str(otx.get("pulse_count"))
        )

        table.add_row(
            "ASN",
            str(otx.get("asn"))
        )

        table.add_row(
            "Country",
            str(otx.get("country"))
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
