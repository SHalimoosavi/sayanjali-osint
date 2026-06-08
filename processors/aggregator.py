import asyncio
import time
from datetime import datetime
from models import OSINTReport, Location, GeoIPResult, Address, ReverseGeocodeResult, ForwardGeocodeResult, DomainResult
from validators import detect_query_type, resolve_domain_to_ip
from apis.ip_geolocation import lookup_ip
from apis.nominatim import reverse_geocode, forward_geocode
from apis.overpass import search_places

async def run_investigation(query: str, nearby_type: str = None, radius: int = 500) -> dict:
    start_time = time.time()
    q_type, norm_query = detect_query_type(query)
    sources = []
    errors = []
    
    report = {"query": query, "query_type": q_type, "timestamp": datetime.now().isoformat(), "sources_queried": [], "errors": []}
    
    if q_type == "ip":
        sources.append("ip_geolocation")
        ip_data = await lookup_ip(norm_query)
        report["ip_geolocation"] = ip_data
        report["latitude"] = ip_data.get("latitude")
        report["longitude"] = ip_data.get("longitude")
        
    elif q_type == "domain":
        sources.append("dns")
        try:
            ip = resolve_domain_to_ip(norm_query)
            report["domain_info"] = {"domain": norm_query, "primary_ip": ip, "all_ips": [ip]}
            sources.append("ip_geolocation")
            ip_data = await lookup_ip(ip)
            report["ip_geolocation"] = ip_data
            report["latitude"] = ip_data.get("latitude")
            report["longitude"] = ip_data.get("longitude")
        except Exception as e:
            errors.append(str(e))
            
    elif q_type == "coordinates":
        lat, lon = map(float, norm_query.split(","))
        report["latitude"], report["longitude"] = lat, lon
        sources.append("reverse_geocoding")
        rev_data = await reverse_geocode(lat, lon)
        report["reverse_geocode"] = rev_data
        
    elif q_type == "address":
        sources.append("forward_geocoding")
        fwd_data = await forward_geocode(norm_query)
        report["forward_geocode"] = fwd_data
        if "latitude" in fwd_data:
            report["latitude"] = fwd_data["latitude"]
            report["longitude"] = fwd_data["longitude"]
            
    if nearby_type and "latitude" in report and report["latitude"]:
        sources.append("overpass_poi")
        poi_data = await search_places(report["latitude"], report["longitude"], nearby_type, radius)
        report["nearby_places"] = poi_data
        
    report["sources_queried"] = sources
    report["errors"] = errors
    report["processing_time_seconds"] = round(time.time() - start_time, 2)
    report["confidence_score"] = 0.8 if not errors else 0.5
    
    return report
