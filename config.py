import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.absolute()
DATA_DIR = PROJECT_ROOT / "data"
CACHE_DIR = PROJECT_ROOT / ".cache"

DATA_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

API_ENDPOINTS = {
    "nominatim": {"reverse": "https://nominatim.openstreetmap.org/reverse", "forward": "https://nominatim.openstreetmap.org/search"},
    "overpass": {"query": "https://overpass-api.de/api/interpreter"},
    "ipapi": {"api": "http://ip-api.com/json/"}
}

GEOIP_DB_PATH = DATA_DIR / "GeoLite2-City.mmdb"
CACHE_DB = CACHE_DIR / "osint_cache.db"

DEFAULT_HEADERS = {"User-Agent": "SAYANJALI-OSINT/1.0 (+http://sayanjali.com)", "Accept": "application/json"}
