import asyncio
import click
import json
import os

from processors.aggregator import run_investigation

from formatters.cli_formatter import format_cli
from formatters.json_formatter import format_json
from formatters.html_formatter import format_html
from formatters.pdf_formatter import generate_pdf


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
    help="Batch file"
)
def main(
    query,
    q_type,
    nearby,
    radius,
    out_format,
    output,
    setup,
    batch
):

    if setup:

        print(
            "📦 Setting up SAYANJALI OSINT..."
        )

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

        print(
            "⬇️ Downloading GeoIP database..."
        )

        urllib.request.urlretrieve(
            url,
            "data/GeoLite2-City.mmdb"
        )

        print(
            "✅ Setup complete"
        )

        return

    if batch:

        with open(
            batch,
            "r"
        ) as f:

            queries = [
                line.strip()
                for line in f
                if line.strip()
            ]

        results = []

        for q in queries:

            result = asyncio.run(
                run_investigation(
                    q,
                    nearby,
                    radius
                )
            )

            results.append(result)

        print(
            json.dumps(
                results,
                indent=2
            )
        )

        return

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

    # TABLE OUTPUT

    if out_format == "table":

        format_cli(report)

        return

    # PDF OUTPUT

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

    # JSON OUTPUT

    if out_format == "json":

        out_data = format_json(
            report
        )

    # HTML OUTPUT

    elif out_format == "html":

        out_data = format_html(
            report
        )

    # CSV OUTPUT

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
