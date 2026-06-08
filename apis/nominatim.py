import urllib.parse
import asyncio
import aiohttp
from config import API_ENDPOINTS, DEFAULT_HEADERS

async def reverse_geocode(lat: float, lon: float) -> dict:
    url = f"{API_ENDPOINTS['nominatim']['reverse']}?format=json&lat={lat}&lon={lon}"
    headers = {**DEFAULT_HEADERS, "Accept-Language": "en"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    addr = data.get("address", {})
                    return {
                        "latitude": lat, "longitude": lon,
                        "full_address": data.get("display_name", ""),
                        "city": addr.get("city") or addr.get("town") or addr.get("village"),
                        "country": addr.get("country", "Unknown"),
                        "country_code": addr.get("country_code", "XX").upper(),
                        "place_name": data.get("name", ""),
                        "confidence": 0.85
                    }
    except Exception as e:
        return {"error": str(e)}
    return {}

async def forward_geocode(query: str) -> dict:
    url = f"{API_ENDPOINTS['nominatim']['forward']}?format=json&q={urllib.parse.quote(query)}&limit=1"
    headers = {**DEFAULT_HEADERS, "Accept-Language": "en"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    if data:
                        d = data[0]
                        return {
                            "query": query, "latitude": float(d["lat"]), "longitude": float(d["lon"]),
                            "full_address": d.get("display_name", ""),
                            "place_type": d.get("type", "unknown"), "confidence": 0.8
                        }
    except Exception as e:
        return {"error": str(e)}
    return {}
