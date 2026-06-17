<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1f2e,100:0f172a&height=200&section=header&text=SAYANJALI%20OSINT&fontSize=52&fontColor=38bdf8&fontAlignY=38&desc=v2.1%20Sentinel%20Intelligence%20—%20Enterprise%20OSINT%20Platform&descColor=94a3b8&descAlignY=58&descSize=15" width="100%"/>

<br/>

[![Version](https://img.shields.io/badge/version-v2.1.0--Sentinel%20Intelligence-38bdf8?style=for-the-badge&logo=git&logoColor=white)](https://github.com/SHalimoosavi/sayanjali-osint/releases)
[![Status](https://img.shields.io/badge/status-Stable%20Release-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)](https://github.com/SHalimoosavi/sayanjali-osint)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20%7C%20macOS%20%7C%20Windows-e2e8f0?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/SHalimoosavi/sayanjali-osint)

<br/>

> **Intelligence. Visibility. Correlation.**
>
> *The intelligence gap between a security analyst and an adversary is closed by the tools they wield.*

<br/>

[📖 What's New](#-whats-new-in-v21-sentinel-intelligence) · [🚀 Install](#-installation) · [⚡ Usage](#-usage--core-capabilities) · [🧠 Modules](#-threat-intelligence-modules) · [👤 Author](#-author--maintainer)

</div>

---

## 🎯 The Problem We're Solving

Security analysts and investigators face a fragmented intelligence landscape. When a threat appears — a suspicious IP, an unknown domain, a malicious actor — the workflow looks like this:

```
VirusTotal → Manual Copy → Shodan → Manual Copy → AbuseIPDB → Manual Copy → Spreadsheet → Report
```

**This is broken.** Investigators waste hours correlating data across 6–10 separate platforms, manually copy-pasting between tabs, and still miss cross-source correlations that only emerge when intelligence is unified — and even after gathering everything, raw data without a reputation match or risk score doesn't tell them whether a target is actually dangerous.

**SAYANJALI OSINT v2.1 Sentinel Intelligence solves this end-to-end:**

| Old Workflow | SAYANJALI OSINT v2.1 |
|---|---|
| 6+ browser tabs | Single CLI command |
| Manual correlation | Automated IOC Risk Engine |
| Raw, unscored data | Reputation-matched threat verdicts |
| No unified report | CLI / JSON / HTML / PDF reporting |
| Hours per investigation | Minutes per investigation |
| Scattered IOC data | Built-in reputation database + cache layer |

---

## 🛡️ Overview

**SAYANJALI OSINT** is an enterprise-grade Open Source Intelligence platform designed to **collect, enrich, correlate, and analyze** intelligence from multiple public data sources.

The platform enables investigators, security analysts, SOC teams, cybersecurity consultants, and researchers to perform rapid intelligence gathering and threat assessment from a single interface — no more switching between a dozen browser tabs to build one picture of a target.

---

## 🆕 What's New in v2.1 Sentinel Intelligence

### Phase 17 Additions

**🧮 IOC Risk Engine**
Evaluates IOC count, VirusTotal results, AbuseIPDB scores, and threat intelligence matches to produce a **Risk Score**, **Risk Classification**, and **Threat Verdict** — automatically, with no manual correlation required.

**🔗 Threat Feed Correlation Engine**
Compares every discovered indicator against the internal reputation database, detecting malicious IPs, domains, emails, and URLs, and outputting a **Threat Score** and **Correlation Verdict**.

**🧠 Sentinel Intelligence Layer**
A new correlation layer fusing signal across IOC extraction, threat reputation data, VirusTotal, AbuseIPDB, AlienVault OTX, and Shodan intelligence into one verdict.

**🌍 Geolocation Intelligence Expansion**
Now supports forward geocoding (place name → coordinates), reverse geocoding (coordinates → place name), and nearby place discovery — directly from the CLI.

**🗄️ Built-In Reputation Database**
Ships with a local threat reputation store covering malicious IP indicators, domains, emails, and URLs.

**💻 Expanded Platform Support**
Officially supports Linux, Termux (Android), macOS, and Windows, on Python 3.11+.

---

## ⚙️ Usage & Core Capabilities

### Domain Intelligence
WHOIS lookup · DNS enumeration · ASN identification · subdomain discovery · reverse DNS analysis · geolocation mapping

```bash
python main.py -q google.com
```

### IP Intelligence
Geolocation · ASN analysis · reverse DNS · VirusTotal reputation · AbuseIPDB reputation · AlienVault OTX intelligence · Shodan intelligence

```bash
python main.py -q 8.8.8.8
```

### Geolocation Intelligence
Forward geocoding, reverse geocoding, and nearby place discovery.

```bash
python main.py -q "Hyderabad, India"
python main.py -q "17.3850,78.4867"
```

---

## 🕵️ Threat Intelligence Modules

| Integration | Provides |
|---|---|
| **VirusTotal** | Reputation analysis · malicious / suspicious / harmless detection counts |
| **AbuseIPDB** | Abuse confidence score · historical abuse reports · ISP & domain information |
| **AlienVault OTX** | Threat pulse correlation · reputation analysis · ASN data · country intelligence |
| **Shodan** | Open ports · exposed services · organization information · host intelligence |

### IOC Analysis Engine
Automatically extracts IP addresses, domains, URLs, and email addresses, generating a consolidated IOC report.

### IOC Risk Engine
Evaluates IOC count, VirusTotal results, AbuseIPDB scores, and threat intelligence matches → outputs **Risk Score**, **Risk Classification**, **Threat Verdict**.

### Threat Feed Correlation
Compares indicators against the internal reputation database → detects malicious IPs, domains, emails, and URLs → outputs **Threat Score** and **Correlation Verdict**.

### Email Intelligence
Email discovery · domain analysis · SPF detection · DMARC detection

### Username Intelligence
Checks username presence across GitHub, GitLab, Reddit, DockerHub, Medium, HackerOne, and Keybase.

---

## 📊 Reporting

| Format | Command |
|---|---|
| CLI Report | `python main.py -q google.com` |
| JSON Report | `python main.py -q google.com -f json` |
| HTML Report | `python main.py -q google.com -f html` |
| PDF Report | `python main.py -q google.com -f pdf` |

---

## ⚡ Performance

**Cache System** — local SQLite cache reduces repeated API calls and speeds up subsequent investigations of the same target.

```bash
python main.py --health           # System diagnostics
python main.py --stats            # Cache statistics
python main.py --cleanup-cache    # Clear expired cache entries
python main.py --batch targets.txt  # Investigate multiple targets at once
```

---

## 📦 Installation

### System Requirements

| Requirement | Version |
|---|---|
| Python | 3.11+ |
| Platforms | Linux · Termux (Android) · macOS · Windows |

### Linux / macOS

```bash
git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint

pip install -r requirements.txt
python main.py --setup
```

### Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y

git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint

pip install -r requirements.txt
python main.py --setup
```

### Windows (PowerShell)

```powershell
git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint

pip install -r requirements.txt
python main.py --setup
```

### API Keys Configuration

After running `--setup`, add your keys to `config.py`:

```python
VIRUSTOTAL_API_KEY = "your_key_here"   # Free tier: virustotal.com
SHODAN_API_KEY      = "your_key_here"   # Free tier: shodan.io
ABUSEIPDB_API_KEY   = "your_key_here"   # Free tier: abuseipdb.com
OTX_API_KEY         = "your_key_here"   # Free tier: otx.alienvault.com
```

> 💡 All four APIs have free tiers. The platform works with partial keys — more keys unlock richer correlation in the Sentinel Intelligence Layer.

> ⚠️ **Security note:** if a `.env` file is tracked in this repository and contains real keys, rotate them immediately and add `.env` to `.gitignore` — deleting a tracked file does not remove it from git history.

---

## 🏗️ Architecture

```
sayanjali-osint/
│
├── apis/                  ← External API clients (VT, Shodan, AbuseIPDB, OTX)
├── cache/                 ← SQLite local cache engine
├── data/                  ← Reputation database & intelligence data models
├── formatters/            ← Output renderers (CLI, HTML, PDF, JSON)
├── processors/            ← IOC Risk Engine + Threat Correlation Engine
├── utils/                 ← Shared utilities & helpers
│
├── main.py
├── config.py
├── validators.py
├── models.py
│
├── requirements.txt
├── VERSION
└── README.md
```

---

## 📈 Version Information

| | |
|---|---|
| **Product** | SAYANJALI OSINT |
| **Release** | v2.1 — Sentinel Intelligence |
| **Status** | Stable Release |
| **Maintained By** | Syed Ali Hasan Moosavi |
| **Organization** | SAYANJALI NEXUS PRIVATE LIMITED |

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
```

Welcome contribution areas: new API integrations (GreyNoise, SecurityTrails, Censys), reputation database expansion, additional output formatters, Windows/macOS compatibility testing, Termux patches.

---

## 🏢 About SAYANJALI NEXUS PRIVATE LIMITED

SAYANJALI OSINT is one of several projects under **SAYANJALI NEXUS PRIVATE LIMITED**, a technology company operating across AI, SaaS, cybersecurity, and blockchain.

| Project | Description |
|---|---|
| [**SYJ ONE**](https://github.com/SHalimoosavi/syj-one) | All-in-one productivity + dev + security platform for Termux |
| [**termux-pro**](https://github.com/SHalimoosavi/termux-pro) | Termux Zero → Pro: Android Dev + Hacking + AI Lab |
| [**moosavi**](https://github.com/SHalimoosavi/moosavi) | Personal portfolio — Three.js blockchain universe |
| [**podcaster_crew**](https://github.com/SHalimoosavi/podcaster_crew) | Multi-agent AI podcast production system |

---

## 👤 Author & Maintainer

<div align="center">

<img src="https://avatars.githubusercontent.com/u/228988824?v=4" width="100" style="border-radius:50%"/>

### Syed Ali Hasan Moosavi

**Founder & Maintainer — SAYANJALI NEXUS PRIVATE LIMITED**

[![GitHub](https://img.shields.io/badge/GitHub-SHalimoosavi-181717?style=for-the-badge&logo=github)](https://github.com/SHalimoosavi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077b5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/syed-ali-hasan-moosavi-237734378/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-f97316?style=for-the-badge&logo=firefox&logoColor=white)](https://shalimoosavi.github.io/moosavi/)
[![X](https://img.shields.io/badge/X-@SHAliMoosavi-000000?style=for-the-badge&logo=x)](https://x.com/SHAliMoosavi)

📍 Hyderabad, India

</div>

---

## 📜 License

MIT License — Copyright (c) 2026 SAYANJALI NEXUS PRIVATE LIMITED. Full text: [LICENSE](LICENSE)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1a1f2e,100:0d1117&height=100&section=footer" width="100%"/>

**SAYANJALI OSINT v2.1 — Sentinel Intelligence**

*Intelligence. Visibility. Correlation.*

⭐ If this tool helped your investigation, star the repo and share it with your team.

</div>
