from rich.console import Console
from rich.panel import Panel


def format_cli(report: dict):
    console = Console()

    console.print(
        Panel(
            f"SAYANJALI OSINT Report\n"
            f"Query: {report.get('query')}\n"
            f"Type: {report.get('query_type')}\n"
            f"Time: {report.get('processing_time_seconds')}s",
            expand=False
        )
    )

    if report.get("ai_summary"):
        console.print(report["ai_summary"])

    if report.get("shodan"):
        console.print(report["shodan"])

    if report.get("virustotal"):
        console.print(report["virustotal"])

    if report.get("errors"):
        console.print(report["errors"])
