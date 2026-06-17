<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1f2e,100:0f172a&height=200&section=header&text=SAYANJALI%20OSINT&fontSize=52&fontColor=38bdf8&fontAlignY=38&desc=v2.1%20Sentinel%20Intelligence%20—%20Enterprise%20OSINT%20Platform&descColor=94a3b8&descAlignY=58&descSize=15" width="100%"/>

<br/>

[![Version](https://img.shields.io/badge/version-v2.1.0--Sentinel%20Intelligence-38bdf8?style=for-the-badge&logo=git&logoColor=white)](https://github.com/SHalimoosavi/sayanjali-osint/releases)
[![Status](https://img.shields.io/badge/status-Stable%20Release-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)](https://github.com/SHalimoosavi/sayanjali-osint)
[![Readiness](https://img.shields.io/badge/production%20readiness-90%25-facc15?style=for-the-badge&logo=target&logoColor=black)](https://github.com/SHalimoosavi/sayanjali-osint)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux-e2e8f0?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/SHalimoosavi/sayanjali-osint)

<br/>

> **Intelligence. Visibility. Correlation.**
>
> *The intelligence gap between a security analyst and an adversary is closed by the tools they wield.*

<br/>

[📖 What's New](#-whats-new-in-v21-sentinel-intelligence) · [🚀 Install](#-installation) · [⚡ Usage](#-usage) · [🧠 Features](#-core-features) · [👤 Author](#-author--maintainer)

</div>

---

## 🎯 The Problem We're Solving

Security analysts and investigators face a fragmented intelligence landscape. When a threat appears — a suspicious IP, an unknown domain, a malicious actor — the workflow looks like this:

```
VirusTotal → Manual Copy → Shodan → Manual Copy → AbuseIPDB → Manual Copy → Spreadsheet → Report
```

**This is broken.** Investigators waste hours correlating data across 6–10 separate platforms, manually copy-pasting between tabs, and still miss cross-source correlations that only emerge when intelligence is unified — and even when they do gather everything, raw data without a reputation match or risk score doesn't tell them whether a target is actually dangerous.

**SAYANJALI OSINT v2.1 Sentinel Intelligence solves this end-to-end:**

| Old Workflow | SAYANJALI OSINT v2.1 |
|---|---|
| 6+ browser tabs | Single CLI command |
| Manual correlation | Automated IOC Risk Engine |
| Raw, unscored data | Reputation-matched threat verdicts |
| No unified report | AI Executive Summary + PDF/HTML/JSON |
| Hours per investigation | Minutes per investigation |
| Scattered IOC data | Built-in reputation database + cache layer |

---

## 🛡️ What Is SAYANJALI OSINT?

**SAYANJALI OSINT** is an enterprise-grade Open Source Intelligence platform built for cybersecurity professionals, SOC analysts, threat hunters, red/blue teams, penetration testers, digital investigators, and OSINT researchers.

**v2.1 Sentinel Intelligence** is a stable release at **90% production readiness**, introducing a dedicated threat correlation layer on top of the v2.0 foundation — moving the platform from "data aggregator" to "automated threat verdict engine."

---

## 🆕 What's New in v2.1 Sentinel Intelligence

### Phase 17 Additions

**🧮 IOC Risk Engine**
Analyzes every extracted Indicator of Compromise and calculates a dynamic threat score, generating an automated verdict instead of leaving correlation to the analyst.

**🔗 Threat Feed Correlation Engine**
Matches discovered indicators against internal reputation databases to identify known malicious infrastructure before you've even opened a second tab.

**🧠 Sentinel Intelligence Layer**
A new correlation layer that fuses signal across:
```
IOC Extraction  ×  Threat Reputation Data  ×  VirusTotal
×  AbuseIPDB  ×  AlienVault OTX  ×  Shodan Intelligence
```

**📋 Enhanced AI Executive Summary**
Every investigation now produces:
- Threat Verdicts
- Risk Scores
- Confidence Levels
- Automated Investigation Findings
- Threat Correlation Results

**🗄️ Built-In Reputation Database**
Ships with a local threat reputation store covering:
- Malicious IP indicators
- Malicious domains
- Malicious emails
- Malicious URLs

---

## ⚙️ Core Features

### Intelligence Collection
```
✓ IP Address Intelligence       ✓ Domain Intelligence
✓ WHOIS Analysis                ✓ DNS Enumeration
✓ ASN Intelligence               ✓ Reverse DNS Resolution
✓ Geolocation Intelligence       ✓ Nearby Location Intelligence
✓ Subdomain Enumeration
```

### Threat Intelligence
| Integration | Capabilities |
|---|---|
| **VirusTotal** | Reputation scoring · malicious/suspicious detection counts |
| **Shodan** | Open ports · service banners · OS fingerprinting |
| **AbuseIPDB** | Abuse confidence score · historical reports · ISP data |
| **AlienVault OTX** | Community pulses · indicator reputation · threat feeds |
| **Reputation Correlation** | Cross-source threat reputation matching |
| **IOC Risk Assessment Engine** | Dynamic scoring across all extracted indicators |

### IOC Analysis
```
✓ IP Extraction          ✓ Domain Extraction
✓ Email Extraction       ✓ URL Extraction
✓ Automated IOC Classification
✓ IOC Risk Scoring
```

### Advanced Correlation
```
✓ Known Malicious IP Detection         ✓ Known Malicious Domain Detection
✓ Known Malicious Email Detection      ✓ Known Malicious URL Detection
✓ Threat Feed Correlation Engine       ✓ Reputation Database Matching
```

### Intelligence Enrichment
```
✓ Email Intelligence Analysis     ✓ SPF Detection
✓ DMARC Detection                  ✓ Username Intelligence
✓ Multi-Platform Username Discovery (GitHub, GitLab, Reddit, DockerHub, HackerOne, Medium, Keybase)
```

### Reporting
```
┌──────────────────────────────────────────────────────────────────┐
│  AI Executive Summary  │  Risk & Confidence Scoring  │  CLI Dashboard │
│  JSON Reports          │  HTML Reports                │  PDF Reports   │
└──────────────────────────────────────────────────────────────────┘
```

### Performance
```
✓ Local Cache System            ✓ Fast Intelligence Aggregation
✓ Modular Architecture           ✓ Async Intelligence Collection
```

---

## 📦 Installation

### Prerequisites

| Requirement | Version | Check |
|---|---|---|
| Python | 3.10+ | `python3 --version` |
| pip | Latest | `pip --version` |
| Git | Any | `git --version` |

### Linux / Kali / Ubuntu

```bash
# Clone the repository
git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint

# Install dependencies
pip install -r requirements.txt

# Run initial setup
python main.py --setup
```

### Termux (Android)

```bash
# Update Termux packages
pkg update && pkg upgrade -y
pkg install python git -y

# Clone and install
git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint

pip install -r requirements.txt
python main.py --setup
```

### API Keys Configuration

SAYANJALI OSINT integrates with threat intelligence APIs. After running `--setup`, add your keys to `config.py` — **not** to `.env` if that file is tracked in your repo (see ⚠️ note below):

```python
VIRUSTOTAL_API_KEY    = "your_key_here"   # Free tier: virustotal.com
SHODAN_API_KEY        = "your_key_here"   # Free tier: shodan.io
ABUSEIPDB_API_KEY     = "your_key_here"   # Free tier: abuseipdb.com
OTX_API_KEY           = "your_key_here"   # Free tier: otx.alienvault.com
```

> 💡 All four APIs have free tiers. The platform works with partial keys — more keys unlock richer correlation in the Sentinel Intelligence Layer.

> ⚠️ **Security note:** your repository currently has a `.env` file committed at the root. If it contains real API keys, rotate them immediately and add `.env` to `.gitignore` going forward — committed secrets remain in git history even after deletion unless the history itself is rewritten.

---

## 🚀 Usage

```bash
# Investigate a domain
python main.py -q google.com

# Investigate an IP address
python main.py -q 8.8.8.8

# Batch investigation (multiple targets from a file)
python main.py --batch targets.txt

# Export as JSON (for automation / SIEM integration)
python main.py -q github.com -f json

# Generate interactive HTML dashboard
python main.py -q github.com -f html -o report.html

# Generate executive PDF report (AI summary + risk score + verdict)
python main.py -q github.com -f pdf

# Run a system health check
python main.py --health

# View cache statistics
python main.py --stats

# Clear expired cache entries
python main.py --cleanup-cache
```

### Reading a Sentinel Intelligence Result

Every investigation under v2.1 now returns:

```
Target          → google.com
Risk Score       → 4 / 100
Threat Verdict   → BENIGN
Confidence       → High
Reputation Match → No match in malicious indicator database
Findings         → AI-generated executive summary of the investigation
```

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
├── main.py                ← CLI entrypoint
├── config.py               ← API keys & platform configuration
├── validators.py           ← Input validation (IP, domain, URL, email)
├── models.py               ← Pydantic data models
│
├── requirements.txt
├── VERSION
└── README.md
```

---

## 📊 Current Release Status

| | |
|---|---|
| **Version** | v2.1.0 — Sentinel Intelligence |
| **Status** | Stable Release |
| **Production Readiness** | 90% |
| **Designed For** | Security Researchers · SOC Teams · Threat Hunters · Blue Teams · Red Teams · Cybersecurity Consultants · Digital Investigators · OSINT Analysts |

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
# → Open a Pull Request
```

**Welcome contribution areas:**
- New API integrations (GreyNoise, SecurityTrails, Censys)
- Expansion of the built-in reputation database
- Additional output formatters
- Performance improvements to the Sentinel Intelligence correlation layer
- Termux compatibility patches

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

**SAYANJALI OSINT v2.1.0 — Sentinel Intelligence**

*Intelligence. Visibility. Correlation.*

⭐ If this tool helped your investigation, star the repo and share it with your team.

</div>
