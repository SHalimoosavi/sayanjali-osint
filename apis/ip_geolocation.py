import asyncio
import aiohttp
import geoip2.database
from config import GEOIP_DB_PATH, API_ENDPOINTS, DEFAULT_HEADERS

async def lookup_ip(ip: str) -> dict:
    result = {"ip": ip, "country": "Unknown", "country_code": "XX", "city": "Unknown", "latitude": 0.0, "longitude": 0.0, "isp": "Unknown", "confidence": 0.5}
    
    # Try MaxMind Local First
    if GEOIP_DB_PATH.exists():
        try:
            with geoip2.database.Reader(str(GEOIP_DB_PATH)) as reader:
                response = reader.city(ip)
                result.update({
                    "country": response.country.name or "Unknown",
                    "country_code": response.country.iso_code or "XX",
                    "region": response.subdivisions[0].name if response.subdivisions else None,
                    "city": response.city.name or "Unknown",
                    "latitude": response.location.latitude or 0.0,
                    "longitude": response.location.longitude or 0.0,
                    "timezone": response.location.time_zone,
                    "confidence": 0.9
                })
                return result
        except Exception:
            pass # Fallback to API

    # Fallback to IP-API (Free, no key)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API_ENDPOINTS['ipapi']['api']}{ip}", headers=DEFAULT_HEADERS, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    result.update({
                        "country": data.get("country", "Unknown"),
                        "country_code": data.get("countryCode", "XX"),
                        "region": data.get("regionName"),
                        "city": data.get("city", "Unknown"),
                        "latitude": float(data.get("lat", 0.0)),
                        "longitude": float(data.get("lon", 0.0)),
                        "isp": data.get("org", "Unknown"),
                        "timezone": data.get("timezone"),
                        "confidence": 0.8
                    })
    except Exception as e:
        result["errors"] = [str(e)]
    return result
