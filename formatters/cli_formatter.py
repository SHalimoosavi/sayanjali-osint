from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

def format_cli(report: dict):
    console = Console()
    console.print(Panel(f"[bold cyan]SAYANJALI OSINT Report[/bold cyan]\nQuery: [yellow]{report['query']}[/yellow] ({report['query_type']})\nTime: {report['processing_time_seconds']}s", expand=False))
    
    if report.get("ip_geolocation"):
        ip = report["ip_geolocation"]
        table = Table(title="IP Geolocation")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")
        table.add_row("IP", ip.get("ip", "N/A"))
        table.add_row("Location", f"{ip.get('city', 'N/A')}, {ip.get('region', 'N/A')}, {ip.get('country', 'N/A')}")
        table.add_row("Coordinates", f"{ip.get('latitude')}, {ip.get('longitude')}")
        table.add_row("ISP", ip.get("isp", "N/A"))
        console.print(table)
        
    if report.get("reverse_geocode"):
        rev = report["reverse_geocode"]
        console.print(Panel(f"[bold]Address:[/bold] {rev.get('full_address', 'N/A')}", title="Reverse Geocode", expand=False))
        
    if report.get("nearby_places"):
        poi = report["nearby_places"]
        table = Table(title=f"Nearby {poi.get('place_type', 'Places')}")
        table.add_column("Name", style="cyan")
        table.add_column("Distance", style="green")
        for p in poi.get("results", [])[:5]:
            table.add_row(p.get("name", "Unknown"), f"{p.get('distance_meters', 'N/A')}m")
        console.print(table)
        
    if report.get("errors"):
        console.print(f"[red]Errors: {', '.join(report['errors'])}[/red]")
