from rich.console import Console
from rich.table import Table
from rich.panel import Panel


def format_cli(report: dict):

    console = Console()

    console.print(
        Panel(
            f"[bold cyan]SAYANJALI OSINT Report[/bold cyan]\n"
            f"Query: [yellow]{report['query']}[/yellow] "
            f"({report['query_type']})\n"
            f"Time: {report['processing_time_seconds']}s",
            expand=False
        )
    )

    # DOMAIN INFO

    if report.get("domain_info"):

        domain = report["domain_info"]

        table = Table(title="Domain Information")

        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        table.add_row(
            "Domain",
            domain.get("domain", "N/A")
        )

        table.add_row(
            "Primary IP",
            domain.get("primary_ip", "N/A")
        )

        console.print(table)

    # WHOIS

    if report.get("whois"):

        whois = report["whois"]

        table = Table(title="WHOIS Information")

        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        table.add_row(
            "Registrar",
            str(whois.get("registrar", "N/A"))
        )

        table.add_row(
            "Creation Date",
            str(whois.get("creation_date", "N/A"))
        )

        table.add_row(
            "Expiration Date",
            str(whois.get("expiration_date", "N/A"))
        )

        table.add_row(
            "Updated Date",
            str(whois.get("updated_date", "N/A"))
        )

        console.print(table)

    # REVERSE DNS

    if report.get("reverse_dns"):

        rdns = report["reverse_dns"]

        if not rdns.get("error"):

            table = Table(title="Reverse DNS")

            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green")

            table.add_row(
                "Hostname",
                rdns.get("hostname", "N/A")
            )

            table.add_row(
                "Addresses",
                ", ".join(
                    rdns.get("addresses", [])
                )
            )

            console.print(table)

    # ASN

    if report.get("asn_info"):

        asn = report["asn_info"]

        if not asn.get("error"):

            table = Table(title="ASN Intelligence")

            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green")

            table.add_row(
                "ASN",
                asn.get("asn", "N/A")
            )

            table.add_row(
                "Organization",
                asn.get("organization", "N/A")
            )

            table.add_row(
                "Network",
                asn.get("network", "N/A")
            )

            table.add_row(
                "Country",
                asn.get("country", "N/A")
            )

            console.print(table)

    # VIRUSTOTAL

    if report.get("virustotal"):

        vt = report["virustotal"]

        malicious = int(
            vt.get("malicious", 0)
        )

        suspicious = int(
            vt.get("suspicious", 0)
        )

        if malicious > 0:
            verdict = "MALICIOUS"
        elif suspicious > 0:
            verdict = "SUSPICIOUS"
        else:
            verdict = "CLEAN"

        table = Table(
            title="VirusTotal Intelligence"
        )

        table.add_column(
            "Field",
            style="cyan"
        )

        table.add_column(
            "Value",
            style="green"
        )

        table.add_row(
            "Reputation",
            str(vt.get("reputation", "N/A"))
        )

        table.add_row(
            "Harmless",
            str(vt.get("harmless", "N/A"))
        )

        table.add_row(
            "Malicious",
            str(vt.get("malicious", "N/A"))
        )

        table.add_row(
            "Suspicious",
            str(vt.get("suspicious", "N/A"))
        )

        table.add_row(
            "Undetected",
            str(vt.get("undetected", "N/A"))
        )

        table.add_row(
            "Threat Verdict",
            verdict
        )

        console.print(table)

    # AI SUMMARY

    if report.get("ai_summary"):

        ai = report["ai_summary"]

        table = Table(
            title="AI Threat Summary"
        )

        table.add_column(
            "Field",
            style="cyan"
        )

        table.add_column(
            "Value",
            style="green"
        )

        table.add_row(
            "Risk Score",
            str(ai.get("risk_score", "N/A"))
        )

        table.add_row(
            "Verdict",
            ai.get("verdict", "N/A")
        )

        findings = "\n".join(
            ai.get("findings", [])[:5]
        )

        table.add_row(
            "Findings",
            findings if findings else "None"
        )

        console.print(table)

    # DNS

    if report.get("dns_records"):

        dns = report["dns_records"]

        table = Table(title="DNS Records")

        table.add_column(
            "Type",
            style="cyan"
        )

        table.add_column(
            "Records",
            style="green"
        )

        for record_type in [
            "A",
            "AAAA",
            "MX",
            "TXT",
            "NS"
        ]:

            values = dns.get(
                record_type,
                []
            )

            if values:

                table.add_row(
                    record_type,
                    "\n".join(values[:5])
                )

        console.print(table)

    # GEOLOCATION

    if report.get("ip_geolocation"):

        ip = report["ip_geolocation"]

        table = Table(
            title="IP Geolocation"
        )

        table.add_column(
            "Field",
            style="cyan"
        )

        table.add_column(
            "Value",
            style="green"
        )

        table.add_row(
            "IP",
            ip.get("ip", "N/A")
        )

        table.add_row(
            "Location",
            f"{ip.get('city', 'N/A')}, "
            f"{ip.get('region', 'N/A')}, "
            f"{ip.get('country', 'N/A')}"
        )

        table.add_row(
            "Coordinates",
            f"{ip.get('latitude')}, "
            f"{ip.get('longitude')}"
        )

        table.add_row(
            "ISP",
            ip.get("isp", "N/A")
        )

        console.print(table)

    # REVERSE GEOCODE

    if report.get("reverse_geocode"):

        rev = report["reverse_geocode"]

        if isinstance(rev, dict):

            address = (
                rev.get("full_address")
                or "N/A"
            )

            console.print(
                Panel(
                    f"[bold]Address:[/bold] {address}",
                    title="Reverse Geocode",
                    expand=False
                )
            )

    # NEARBY PLACES

    if report.get("nearby_places"):

        poi = report["nearby_places"]

        table = Table(
            title=f"Nearby {poi.get('place_type', 'Places')}"
        )

        table.add_column(
            "Name",
            style="cyan"
        )

        table.add_column(
            "Distance",
            style="green"
        )

        for place in poi.get(
            "results",
            []
        )[:10]:

            table.add_row(
                place.get(
                    "name",
                    "Unknown"
                ),
                f"{place.get('distance_meters', 'N/A')}m"
            )

        console.print(table)

    # ERRORS

    if report.get("errors"):

        if len(report["errors"]) > 0:

            console.print(
                f"[red]{', '.join(report['errors'])}[/red]"
            )
