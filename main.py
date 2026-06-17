import asyncio
import click
import json
import os

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from processors.aggregator import run_investigation

from formatters.cli_formatter import format_cli
from formatters.json_formatter import format_json
from formatters.html_formatter import format_html
from formatters.pdf_formatter import generate_pdf

from cache.cache_manager import CacheManager
from utils.health_check import run_health_check


console = Console()


@click.command()
@click.option(
    "-q",
    "--query",
    help="IP, Domain, Address, or Coordinates (lat,lon)"
)
@click.option(
    "-t",
    "--type",
    "q_type",
    help="Force query type"
)
@click.option(
    "--nearby",
    help="Search nearby places"
)
@click.option(
    "--radius",
    default=500,
    help="Radius in meters"
)
@click.option(
    "-f",
    "--format",
    "out_format",
    default="table",
    type=click.Choice(
        [
            "table",
            "json",
            "html",
            "csv",
            "pdf"
        ]
    )
)
@click.option(
    "-o",
    "--output",
    help="Output file path"
)
@click.option(
    "--setup",
    is_flag=True,
    help="Download GeoIP database"
)
@click.option(
    "--batch",
    help="Batch file containing targets"
)
@click.option(
    "--health",
    is_flag=True,
    help="Run system health check"
)
@click.option(
    "--stats",
    is_flag=True,
    help="Show cache statistics"
)
@click.option(
    "--cleanup-cache",
    is_flag=True,
    help="Remove expired cache entries"
)
def main(
    query,
    q_type,
    nearby,
    radius,
    out_format,
    output,
    setup,
    batch,
    health,
    stats,
    cleanup_cache
):

    # ==================================================
    # HEALTH CHECK
    # ==================================================

    if health:

        result = run_health_check()

        console.print(
            Panel(
                "SAYANJALI OSINT Health Check",
                title="System Diagnostics"
            )
        )

        for name, status in result["checks"].items():

            if status:
                print(f"[OK] {name}")
            else:
                print(f"[FAIL] {name}")

        print()

        if result["healthy"]:
            print("SYSTEM STATUS: HEALTHY")
        else:
            print("SYSTEM STATUS: DEGRADED")

        return

    # ==================================================
    # CACHE STATS
    # ==================================================

    if stats:

        cache = CacheManager()

        console.print(
            Panel(
                "SAYANJALI OSINT Cache Statistics",
                title="Statistics"
            )
        )

        print(
            f"Cache Entries : {cache.count_entries()}"
        )

        print(
            f"Database Size : {cache.database_size()} KB"
        )

        print(
            "Status         : Production Release"
        )

        return

    # ==================================================
    # CACHE CLEANUP
    # ==================================================

    if cleanup_cache:

        cache = CacheManager()

        removed = cache.cleanup()

        print(
            f"Expired cache removed: {removed}"
        )

        return

    # ==================================================
    # SETUP
    # ==================================================

    if setup:

        print("📦 Setting up SAYANJALI OSINT...")

        os.makedirs(
            "data",
            exist_ok=True
        )

        import urllib.request

        url = (
            "https://github.com/"
            "P3TERPRETER/"
            "GeoLite2-City/raw/main/"
            "GeoLite2-City.mmdb"
        )

        print("⬇️ Downloading GeoIP database...")

        urllib.request.urlretrieve(
            url,
            "data/GeoLite2-City.mmdb"
        )

        print("✅ Setup complete")

        return

    # ==================================================
    # BATCH INTELLIGENCE
    # ==================================================

    if batch:

        with open(
            batch,
            "r",
            encoding="utf-8"
        ) as f:

            targets = [
                line.strip()
                for line in f
                if line.strip()
            ]

        results = []

        completed = 0
        failed = 0
        total_risk = 0

        console.print(
            Panel(
                f"Targets Loaded: {len(targets)}",
                title="Batch Intelligence"
            )
        )

        for target in targets:

            try:

                report = asyncio.run(
                    run_investigation(
                        target,
                        nearby,
                        radius
                    )
                )

                results.append(report)

                completed += 1

                risk = (
                    report
                    .get("ai_summary", {})
                    .get("risk_score", 0)
                )

                total_risk += risk

            except Exception as e:

                failed += 1

                results.append(
                    {
                        "query": target,
                        "error": str(e)
                    }
                )

        table = Table(
            title="Batch Intelligence Summary"
        )

        table.add_column(
            "Target",
            style="cyan"
        )

        table.add_column(
            "Verdict",
            style="green"
        )

        table.add_column("Risk")
        table.add_column("Cache")

        for report in results:

            if report.get("error"):

                table.add_row(
                    report["query"],
                    "FAILED",
                    "-",
                    "-"
                )

                continue

            ai = report.get(
                "ai_summary",
                {}
            )

            table.add_row(
                report.get(
                    "query",
                    "N/A"
                ),
                str(
                    ai.get(
                        "verdict",
                        "Unknown"
                    )
                ),
                str(
                    ai.get(
                        "risk_score",
                        0
                    )
                ),
                report.get(
                    "cache_status",
                    "N/A"
                )
            )

        console.print(table)

        avg_risk = 0

        if completed:

            avg_risk = round(
                total_risk / completed,
                2
            )

        console.print(
            Panel(
                f"Completed : {completed}\n"
                f"Failed : {failed}\n"
                f"Average Risk : {avg_risk}",
                title="Batch Statistics"
            )
        )

        if output:

            with open(
                output,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    results,
                    f,
                    indent=2
                )

            print(
                f"✅ Batch report saved to {output}"
            )

        return

    # ==================================================
    # SINGLE TARGET
    # ==================================================

    if not query:

        click.echo(
            "Use --help for usage."
        )

        return

    report = asyncio.run(
        run_investigation(
            query,
            nearby,
            radius
        )
    )

    # ==================================================
    # TABLE
    # ==================================================

    if out_format == "table":

        format_cli(report)

        return

    # ==================================================
    # PDF
    # ==================================================

    if out_format == "pdf":

        if not output:

            output = (
                f"{query.replace('.', '_')}.pdf"
            )

        generate_pdf(
            report,
            output
        )

        print(
            f"✅ PDF report saved to {output}"
        )

        return

    # ==================================================
    # JSON
    # ==================================================

    if out_format == "json":

        out_data = format_json(
            report
        )

    # ==================================================
    # HTML
    # ==================================================

    elif out_format == "html":

        out_data = format_html(
            report
        )

    # ==================================================
    # CSV
    # ==================================================

    else:

        ip_loc = report.get(
            "ip_geolocation",
            {}
        )

        out_data = (
            "query,"
            "query_type,"
            "latitude,"
            "longitude,"
            "country,"
            "city\n"
        )

        out_data += (
            f"{report.get('query')},"
            f"{report.get('query_type')},"
            f"{report.get('latitude','')},"
            f"{report.get('longitude','')},"
            f"{ip_loc.get('country','')},"
            f"{ip_loc.get('city','')}\n"
        )

    if output:

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(out_data)

        print(
            f"✅ Report saved to {output}"
        )

    else:

        print(out_data)


if __name__ == "__main__":
    main()
