import asyncio
import click
import json
import os
from processors.aggregator import run_investigation
from formatters.cli_formatter import format_cli
from formatters.json_formatter import format_json
from formatters.html_formatter import format_html

@click.command()
@click.option('-q', '--query', help='IP, Domain, Address, or Coordinates (lat,lon)')
@click.option('-t', '--type', 'q_type', help='Force query type (ip, domain, address, coordinates)')
@click.option('--nearby', help='Search for nearby places (e.g., hotel, cafe, hospital)')
@click.option('--radius', default=500, help='Radius for nearby search in meters')
@click.option('-f', '--format', 'out_format', default='table', type=click.Choice(['table', 'json', 'html', 'csv']))
@click.option('-o', '--output', help='Output file path')
@click.option('--setup', is_flag=True, help='Download GeoIP database and setup')
@click.option('--batch', help='Path to file with newline-separated queries')
def main(query, q_type, nearby, radius, out_format, output, setup, batch):
    if setup:
        print("📦 Setting up SAYANJALI OSINT...")
        os.makedirs("data", exist_ok=True)
        import urllib.request
        url = "https://github.com/P3TERPRETER/GeoLite2-City/raw/main/GeoLite2-City.mmdb"
        print(f"⬇️ Downloading GeoIP database to data/GeoLite2-City.mmdb...")
        urllib.request.urlretrieve(url, "data/GeoLite2-City.mmdb")
        print("✅ Setup complete! You can now run queries.")
        return

    if batch:
        with open(batch, 'r') as f:
            queries = [line.strip() for line in f if line.strip()]
        results = []
        for q in queries:
            res = asyncio.run(run_investigation(q, nearby, radius))
            results.append(res)
        out_data = json.dumps(results, indent=2)
    elif query:
        res = asyncio.run(run_investigation(query, nearby, radius))
        if out_format == 'table':
            format_cli(res)
            return
        elif out_format == 'json':
            out_data = format_json(res)
        elif out_format == 'html':
            out_data = format_html(res)
        elif out_format == 'csv':
            out_data = "query,query_type,latitude,longitude,country,city\n"
            ip_loc = res.get("ip_geolocation", {})
            out_data += f"{res.get('query')},{res.get('query_type')},{res.get('latitude', '')},{res.get('longitude', '')},{ip_loc.get('country', '')},{ip_loc.get('city', '')}\n"
    else:
        click.echo("Use --help for usage information or --setup to initialize.")
        return

    if output:
        with open(output, 'w') as f:
            f.write(out_data)
        print(f"✅ Report saved to {output}")
    else:
        print(out_data)

if __name__ == '__main__':
    main()
