<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1f2e,100:0f172a&height=200&section=header&text=SAYANJALI%20OSINT&fontSize=52&fontColor=38bdf8&fontAlignY=38&desc=Open-Source%20Intelligence%20Platform%20v2.0%20Sentinel&descColor=94a3b8&descAlignY=58&descSize=16" width="100%"/>

<br/>

[![Version](https://img.shields.io/badge/version-v2.0.0--Sentinel-38bdf8?style=for-the-badge&logo=git&logoColor=white)](https://github.com/SHalimoosavi/sayanjali-osint/releases)
[![Status](https://img.shields.io/badge/status-Production%20Ready-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)](https://github.com/SHalimoosavi/sayanjali-osint)
[![Python](https://img.shields.io/badge/Python-3.10%2B-facc15?style=for-the-badge&logo=python&logoColor=black)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux-e2e8f0?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/SHalimoosavi/sayanjali-osint)
[![Author](https://img.shields.io/badge/Author-Syed%20Ali%20Hasan%20Moosavi-f97316?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SHalimoosavi)

<br/>

> **Intelligence. Visibility. Correlation.**
> 
> *The intelligence gap between a security analyst and an adversary is closed by the tools they wield.*

<br/>

[📖 Documentation](#-documentation) · [🚀 Quick Start](#-quick-start) · [⚡ Features](#-features) · [🛠 Architecture](#-architecture) · [👤 Author](#-author)

</div>

---

## 🎯 The Problem We're Solving

Security analysts and investigators face a fragmented intelligence landscape. When a threat appears — a suspicious IP, an unknown domain, a malicious actor — the workflow looks like this:

```
VirusTotal → Manual Copy → Shodan → Manual Copy → AbuseIPDB → Manual Copy → Spreadsheet → Report
```

**This is broken.** Investigators waste hours correlating data across 6–10 separate platforms, manually copy-pasting between tabs, and still miss cross-source correlations that only emerge when intelligence is unified.

**SAYANJALI OSINT v2.0 Sentinel solves this:**

| Old Workflow | SAYANJALI OSINT |
|---|---|
| 6+ browser tabs | Single CLI command |
| Manual correlation | Automated threat scoring |
| No unified report | PDF + HTML + JSON export |
| Hours per investigation | Minutes per investigation |
| Scattered IOC data | Unified intelligence database |

---

## 🛡️ What Is SAYANJALI OSINT?

**SAYANJALI OSINT** is a production-grade Open Source Intelligence platform that aggregates threat intelligence, infrastructure data, domain analysis, and reputation scoring from multiple authoritative sources into a single, unified investigation framework.

Built for:
- 🔵 **Security Operations Centers (SOC)** — rapid IOC triage and enrichment
- 🔴 **Penetration Testers** — passive recon without leaving active fingerprints
- 🟡 **Digital Investigators** — multi-source intelligence correlation
- 🟢 **Threat Analysts** — executive-grade reporting with evidence trails
- 🟣 **Bug Bounty Hunters** — efficient target reconnaissance

---

## ⚡ Features

### 🌐 IP & Network Intelligence
```
✓ GeoIP Lookup              ✓ ASN Intelligence
✓ Reverse DNS Analysis      ✓ IP Reputation Scoring
✓ Threat Feed Correlation   ✓ Infrastructure Mapping
```

### 🌍 Domain Intelligence
```
✓ WHOIS Analysis            ✓ DNS Enumeration
✓ Reverse DNS Resolution    ✓ Domain Reputation
✓ Passive Subdomain Enum    ✓ Infrastructure Discovery
```

### 🕵️ Multi-Source Threat Intelligence

| Integration | Capabilities |
|---|---|
| **VirusTotal** | Reputation scoring · Malicious/suspicious detection counts |
| **Shodan** | Open ports · Service banners · OS fingerprinting |
| **AbuseIPDB** | Abuse confidence score · Historical reports · ISP data |
| **AlienVault OTX** | Community pulses · Indicator reputation · Threat feeds |

### 🔍 Passive Reconnaissance Engine
```
✓ Zero active fingerprint — purely passive enumeration
✓ Automated IOC extraction: IPs, Domains, URLs, Emails
✓ Subdomain discovery via DNS-based passive methods
✓ Cross-source indicator correlation
```

### 👤 Username & Identity Intelligence
Cross-platform footprint analysis across:
`GitHub` · `GitLab` · `Reddit` · `DockerHub` · `HackerOne` · `Medium` · `Keybase`

### 🧠 Threat Correlation Engine
The platform's core intelligence layer synthesizes all gathered data into:
- **Risk Score** — quantified threat rating
- **Threat Verdict** — BENIGN / SUSPICIOUS / MALICIOUS / UNKNOWN
- **Confidence Rating** — evidence quality assessment
- **Executive Findings** — human-readable intelligence summary

### 📊 Multi-Format Reporting

```
┌─────────────────────────────────────────────────────────┐
│  CLI Dashboard  │  HTML Report  │  PDF Executive  │  JSON │
│  Rich terminal  │  Interactive  │  Professional   │  API  │
│  Real-time      │  shareable    │  court-ready    │  export│
└─────────────────────────────────────────────────────────┘
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

SAYANJALI OSINT integrates with threat intelligence APIs. After running `--setup`, configure your keys in `config.py`:

```python
VIRUSTOTAL_API_KEY    = "your_key_here"   # Free: virustotal.com
SHODAN_API_KEY        = "your_key_here"   # Free tier: shodan.io
ABUSEIPDB_API_KEY     = "your_key_here"   # Free: abuseipdb.com
OTX_API_KEY           = "your_key_here"   # Free: otx.alienvault.com
```

> 💡 **All API keys have free tiers.** The platform functions with partial keys — more keys = richer intelligence.

---

## 🚀 Quick Start

```bash
# Investigate a domain
python main.py -q google.com

# Investigate an IP address
python main.py -q 8.8.8.8

# Batch investigation (multiple targets)
python main.py --batch targets.txt

# Export as JSON (for automation/integrations)
python main.py -q github.com -f json

# Generate interactive HTML dashboard
python main.py -q github.com -f html -o report.html

# Generate executive PDF report
python main.py -q github.com -f pdf

# System health check
python main.py --health

# Cache statistics
python main.py --stats

# Clean expired cache
python main.py --cleanup-cache
```

---

## 🏗️ Architecture

```
sayanjali-osint/
│
├── apis/                  ← External API clients (VT, Shodan, AbuseIPDB, OTX)
├── cache/                 ← SQLite local cache engine
├── data/                  ← Intelligence data models & storage
├── formatters/            ← Output renderers (CLI, HTML, PDF, JSON)
├── processors/            ← Intelligence correlation & scoring engine
├── utils/                 ← Shared utilities & helpers
│
├── main.py                ← CLI entrypoint
├── config.py              ← API keys & platform configuration
├── validators.py          ← Input validation (IP, domain, URL)
├── models.py              ← Pydantic data models
│
├── requirements.txt
├── VERSION
└── README.md
```

### Performance & Caching

```
First run  → Fetches live data from all APIs → Stores in SQLite cache
Repeat run → Serves from local cache         → Zero API calls, instant results
```

Batch investigations run targets concurrently, drastically reducing total investigation time.

---

## 📈 Roadmap

- [ ] **v2.1** — Telegram & Discord alert integrations
- [ ] **v2.2** — Dark web mention monitoring hooks
- [ ] **v2.3** — MITRE ATT&CK framework tagging
- [ ] **v3.0** — Web UI dashboard (FastAPI + React)
- [ ] **v3.1** — Team collaboration & shared investigations

---

## 🤝 Contributing

Contributions are welcome from the security community.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
# → Open a Pull Request
```

**Areas we welcome contributions:**
- New API integrations (e.g. GreyNoise, SecurityTrails, Censys)
- Additional output formatters
- Performance improvements to the correlation engine
- Termux compatibility patches
- Documentation & usage examples

---

## 🏢 About SAYANJALI NEXUS PRIVATE LIMITED

SAYANJALI OSINT is one of several open-source and commercial projects under **SAYANJALI NEXUS PRIVATE LIMITED**, a technology company operating across AI, SaaS, cybersecurity, and blockchain verticals.

**Other projects by the same author:**

| Project | Description | Stack |
|---|---|---|
| [**SYJ ONE**](https://github.com/SHalimoosavi/syj-one) | All-in-one productivity + dev + security platform for Termux | Python |
| [**NexusRank AI**](https://github.com/SHalimoosavi) | Enterprise SEO/GEO SaaS with multi-provider AI integration | FastAPI + React |
| [**termux-pro**](https://github.com/SHalimoosavi/termux-pro) | Termux Zero → Pro: Android Dev + Hacking + AI Lab | HTML/Shell |
| [**moosavi**](https://github.com/SHalimoosavi/moosavi) | Personal portfolio — Three.js blockchain universe | HTML/JS |
| [**podcaster_crew**](https://github.com/SHalimoosavi/podcaster_crew) | Multi-agent AI podcast production system | Python |

---

## 👤 Author

<div align="center">

<img src="https://avatars.githubusercontent.com/u/228988824?v=4" width="100" style="border-radius:50%"/>

### Syed Ali Hasan Moosavi

**Founder & Managing Director — SAYANJALI NEXUS PRIVATE LIMITED**

*Automation engineer working with N8N, APIs, GitHub Actions, AI agents, and Web3 operations.*
*Building systems that prioritize reliability, observability, and operational clarity.*

[![GitHub](https://img.shields.io/badge/GitHub-SHalimoosavi-181717?style=for-the-badge&logo=github)](https://github.com/SHalimoosavi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077b5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/syed-ali-hasan-moosavi-237734378/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-f97316?style=for-the-badge&logo=firefox&logoColor=white)](https://shalimoosavi.github.io/moosavi/)
[![X](https://img.shields.io/badge/X-@SHAliMoosavi-000000?style=for-the-badge&logo=x)](https://x.com/SHAliMoosavi)

📍 Hyderabad, India · 🕐 UTC +05:30

</div>

---

## 📜 License

```
MIT License
Copyright (c) 2026 SAYANJALI NEXUS PRIVATE LIMITED

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

Full license text: [LICENSE](LICENSE)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1a1f2e,100:0d1117&height=100&section=footer" width="100%"/>

**SAYANJALI OSINT v2.0.0 Sentinel**

*Intelligence. Visibility. Correlation.*

Powered by **[SAYANJALI NEXUS PRIVATE LIMITED](https://shalimoosavi.github.io/moosavi/)**

⭐ If this tool helped your investigation, star the repo and share it with your team.

</div>
