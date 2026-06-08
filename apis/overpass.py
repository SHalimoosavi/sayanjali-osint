import math
import asyncio
import aiohttp
from config import API_ENDPOINTS

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))


async def search_places(lat: float, lon: float, place_type: str, radius: int = 500) -> dict:
    # Approximate degree conversion for bbox
    deg_lat = radius / 111000
    deg_lon = radius / (111000 * abs(__import__('math').cos(lat * __import__('math').pi / 180)) or 1)
    
    query = f"""
    [out:json][timeout:25];
    (
      node["amenity"="{place_type}"](around:{radius},{lat},{lon});
      way["amenity"="{place_type}"](around:{radius},{lat},{lon});
      node["tourism"="{place_type}"](around:{radius},{lat},{lon});
      way["tourism"="{place_type}"](around:{radius},{lat},{lon});
    );
    out center;
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(API_ENDPOINTS['overpass']['query'], data=query, timeout=30) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    results = []
                    for element in data.get("elements", []):
                        if "tags" in element:
                            tags = element["tags"]
                            results.append({
                                "name": tags.get("name", "Unnamed"),
                                "latitude": element.get("lat", element.get("center", {}).get("lat", lat)),
                                "longitude": element.get("lon", element.get("center", {}).get("lon", lon)),
                                "place_type": place_type,
                                "distance_meters": round(haversine(lat, lon, 
                                    element.get("lat", element.get("center", {}).get("lat", lat)), 
                                    element.get("lon", element.get("center", {}).get("lon", lon))))
                            })
                    return {"query": f"{place_type} near {lat},{lon}", "place_type": place_type, "radius_meters": radius, "results": results[:10], "total_results": len(results)}
    except Exception as e:
        return {"error": str(e)}
    return {"results": []}
