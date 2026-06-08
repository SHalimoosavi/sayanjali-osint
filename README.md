# 🔍 SAYANJALI OSINT

**A powerful, command-line geolocation intelligence aggregation tool optimized for Termux (Android).**

SAYANJALI OSINT unifies multiple free and open geolocation APIs to transform a single input (IP, domain, address, coordinates) into comprehensive, investigation-ready location intelligence.

---

## ✨ Features

- 🌍 **IP Geolocation**: Local MaxMind GeoLite2 database with API fallbacks.
- 📍 **Reverse Geocoding**: Convert coordinates to physical addresses (Nominatim/OSM).
- 🗺️ **Forward Geocoding**: Convert addresses or place names to coordinates.
- 🏢 **Nearby POI Search**: Find cafes, hotels, hospitals, etc., near any coordinates (Overpass API).
- 🌐 **Domain Resolution**: Auto-resolves domains to IPs and geolocates the server.
- ⚡ **Async Processing**: Lightning-fast concurrent API queries.
- 📊 **Multiple Outputs**: Beautiful CLI tables, JSON, CSV, and HTML reports with embedded Leaflet maps.
- 📦 **Batch Processing**: Process lists of targets from a text file.
- 📱 **100% Termux Optimized**: No heavy dependencies, runs perfectly on Android.

---

## 📋 Prerequisites

Before you begin, ensure you have the following:
- An Android device (Android 5.0+)
- **[Termux](https://f-droid.org/packages/com.termux/)** installed (⚠️ *Please install from F-Droid, the Play Store version is deprecated and broken*)
- **~50MB** of free storage space
- An active internet connection (for API queries and initial database download)

---

## 🛠️ Installation (Termux)

Follow these steps exactly in your Termux terminal to get up and running:

```bash
# 1. Update your Termux packages
pkg update && pkg upgrade -y

# 2. Install Python, Git, and Curl
pkg install -y python git curl

# 3. Clone the repository
git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint

# 4. Install Python dependencies
pip install -r requirements.txt --no-cache-dir

# 5. Download the MaxMind GeoLite2 Database (Required for IP geolocation)
mkdir -p data
curl -L https://github.com/P3TERPRETER/GeoLite2-City/raw/main/GeoLite2-City.mmdb -o data/GeoLite2-City.mmdb

# 6. Verify the installation by running a test query
python3 main.py --query 8.8.8.8
