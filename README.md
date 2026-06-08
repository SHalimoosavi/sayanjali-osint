<div align="center">

<img src="https://img.shields.io/badge/SAYANJALI-OSINT-00d4ff?style=for-the-badge&labelColor=0a0a0a&color=00d4ff" alt="SAYANJALI OSINT"/>

# 🔍 SAYANJALI OSINT

### *Transforming Public Data into Actionable Geolocation Intelligence*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-brightgreen?style=flat-square&logo=android&logoColor=white)](https://f-droid.org/packages/com.termux/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-SHalimoosavi-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SHalimoosavi)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()

<br/>

> A powerful command-line geolocation intelligence aggregation tool — optimized for **Termux (Android)**.  
> Unifies multiple free and open geolocation APIs to transform a single input into **comprehensive, investigation-ready intelligence**.

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Output Formats](#-output-formats)
- [Configuration](#-configuration)
- [Supported Intelligence Sources](#-supported-intelligence-sources)
- [Troubleshooting](#-troubleshooting)
- [Security & Privacy](#-security--privacy)
- [Roadmap](#-roadmap)
- [Author](#-author)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌐 Overview

**SAYANJALI OSINT** is a lightweight yet powerful OSINT geolocation framework designed for **Android Termux** environments. It aggregates intelligence from multiple free geolocation sources and presents results in investigator-friendly formats.

### Supported Target Types

| Type | Example |
|------|---------|
| 🌐 IP Addresses | `8.8.8.8` |
| 🔗 Domains | `google.com` |
| 📍 GPS Coordinates | `48.8584, 2.2945` |
| 🏠 Physical Addresses | `Eiffel Tower, Paris` |
| 🗺️ Locations & Landmarks | Any named place |

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔎 Geolocation Intelligence
- IP Geolocation
- Domain Resolution
- Reverse Geocoding
- Forward Geocoding
- Nearby Points of Interest Search

### ⚡ Performance
- Async Concurrent Requests
- Fast API Aggregation
- Local GeoLite2 Database Support
- Intelligent Caching

</td>
<td width="50%">

### 📊 Reporting
- Terminal Tables
- JSON Reports
- CSV Exports
- HTML Reports
- Interactive Leaflet Maps

### 🖥️ Platform Support
- Android (Termux) ✅
- Linux ✅
- Ubuntu / Debian ✅
- Kali Linux ✅

</td>
</tr>
</table>

---

## 📦 Prerequisites

Before installation, ensure you have:

| Requirement | Version |
|-------------|---------|
| Android | 5.0+ |
| Termux | F-Droid version (recommended) |
| Python | 3.10+ |
| Git | Latest |
| Curl | Latest |
| Storage | ~50MB free |

> ⚠️ **Important:** The Play Store version of Termux is no longer maintained.  
> Download Termux from F-Droid: [https://f-droid.org/packages/com.termux/](https://f-droid.org/packages/com.termux/)

---

## 🚀 Installation

### Step 1 — Update Packages

```bash
pkg update && pkg upgrade -y
```

### Step 2 — Install Requirements

```bash
pkg install -y python git curl
```

### Step 3 — Clone Repository

```bash
git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint
```

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt --no-cache-dir
```

### Step 5 — Download GeoLite2 Database

```bash
mkdir -p data

curl -L https://github.com/P3TERPRETER/GeoLite2-City/raw/main/GeoLite2-City.mmdb \
  -o data/GeoLite2-City.mmdb
```

### Step 6 — Verify Installation

```bash
python3 main.py --query 8.8.8.8
```

---

## 🛠️ Usage

### Help Menu

```bash
python3 main.py --help
```

### IP Geolocation

```bash
python3 main.py --query 8.8.8.8
```

### Domain Resolution

```bash
python3 main.py --query google.com
```

### Reverse Geocoding

```bash
python3 main.py --query "48.8584,2.2945"
```

### Forward Geocoding

```bash
python3 main.py --query "Eiffel Tower, Paris"
```

### Batch Processing

```bash
python3 main.py --batch targets.txt
```

---

## 📄 Output Formats

| Format | Command |
|--------|---------|
| 📋 Table (default) | `python3 main.py --query google.com` |
| 🗂️ JSON | `python3 main.py --query google.com --format json` |
| 📊 CSV | `python3 main.py --query google.com --format csv` |
| 🌐 HTML Report | `python3 main.py --query google.com --format html` |

---

## ⚙️ Configuration

Create or modify the `.env` file in the project root:

```env
# API Rate Limits
NOMINATIM_RATE_LIMIT=1
OVERPASS_RATE_LIMIT=0.5

# Logging
LOG_LEVEL=INFO

# Default Output Format
DEFAULT_FORMAT=table

# Cache Settings
ENABLE_CACHE=true
CACHE_EXPIRY_HOURS=24
```

---

## 🔗 Supported Intelligence Sources

| Source | Purpose |
|--------|---------|
| [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) | Offline IP Geolocation |
| [OpenStreetMap Nominatim](https://nominatim.org/) | Geocoding (Forward & Reverse) |
| [Overpass API](https://overpass-api.de/) | Nearby Locations & POI |
| DNS Resolver | Domain-to-IP Resolution |
| [Leaflet.js](https://leafletjs.com/) | Interactive Map Rendering |

---

## 🐛 Troubleshooting

### `ModuleNotFoundError`

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### GeoLite2 Database Missing

```bash
mkdir -p data

curl -L https://github.com/P3TERPRETER/GeoLite2-City/raw/main/GeoLite2-City.mmdb \
  -o data/GeoLite2-City.mmdb
```

### API Rate Limit Errors (`HTTP 429`)

If you encounter `429 Too Many Requests`:

- Wait before retrying requests
- Enable caching in `.env` (`ENABLE_CACHE=true`)
- Increase request intervals via rate limit settings

---

## 🔒 Security & Privacy

SAYANJALI OSINT is designed with privacy in mind:

- ✅ Does **not** collect or transmit user data
- ✅ Uses only **public OSINT sources**
- ✅ Supports **local offline** IP geolocation via GeoLite2
- ✅ Minimizes external API calls through intelligent **caching**

> **Users remain solely responsible for legal and ethical usage in their jurisdiction.**

---

## 🗺️ Roadmap

Planned features for upcoming releases:

- [ ] Shodan Integration
- [ ] WHOIS Intelligence
- [ ] ASN Lookup
- [ ] Email Intelligence
- [ ] Phone Number Intelligence
- [ ] Telegram Username Intelligence
- [ ] Social Media Discovery
- [ ] PDF Report Generation
- [ ] AI Investigation Assistant
- [ ] Multi-Language Support

---

## 👤 Author

<div align="center">

**Syed Ali Hasan Moosavi**  
*Founder & Managing Director*  
**SAYANJALI NEXUS PRIVATE LIMITED**

[![GitHub](https://img.shields.io/badge/GitHub-SHalimoosavi-181717?style=for-the-badge&logo=github)](https://github.com/SHalimoosavi)

</div>

### Core Projects

| Project | Description |
|---------|-------------|
| 🔍 SAYANJALI OSINT | Geolocation Intelligence Framework |
| 🪙 SYJ Token | Blockchain Token Ecosystem |
| 🤖 NexusRank AI | Enterprise SEO / GEO AI Platform |
| 🏥 BBG Nexus AI | AI-Powered Business Intelligence |
| 🏨 MA Hospital SaaS | Healthcare Management Platform |

---

## 🤝 Contributing

Contributions are welcome and appreciated!

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📜 License

```
MIT License

Copyright (c) 2026 Syed Ali Hasan Moosavi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software.
```

---

## ⭐ Support

If SAYANJALI OSINT has been useful to you:

- ⭐ **Star** the repository
- 🍴 **Fork** and build upon it
- 📢 **Share** with the OSINT community
- 🐛 **Report** issues and bugs via GitHub Issues

---

<div align="center">

**SAYANJALI OSINT**  
*Powered by [SAYANJALI NEXUS PRIVATE LIMITED](https://github.com/SHalimoosavi)*

</div>
