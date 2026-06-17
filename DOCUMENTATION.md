<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1f2e,100:0f172a&height=200&section=header&text=SAYANJALI%20OSINT&fontSize=52&fontColor=38bdf8&fontAlignY=38&desc=v2.1%20Sentinel%20Intelligence%20—%20Enterprise%20Threat%20Intelligence%20Platform&descColor=94a3b8&descAlignY=58&descSize=14" width="100%"/>

<br/>

[![Version](https://img.shields.io/badge/version-v2.1.0--Sentinel%20Intelligence-38bdf8?style=for-the-badge&logo=git&logoColor=white)](#)
[![Status](https://img.shields.io/badge/status-Stable%20Release-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)](#)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20%7C%20macOS%20%7C%20Windows-e2e8f0?style=for-the-badge&logo=linux&logoColor=black)](#)

<br/>

# Stop investigating threats one tab at a time

**SAYANJALI OSINT turns six hours of manual cross-referencing into one command.** It pulls intelligence from VirusTotal, Shodan, AbuseIPDB, and AlienVault OTX, correlates it automatically, and hands you a risk score and verdict — not a pile of raw data you still have to interpret.

[**📋 See What It Replaces**](#-what-this-replaces) · [**🧠 Explore Capabilities**](#-what-you-get) · [**📞 Get In Touch**](#-get-started)

</div>

---

## 📋 What This Replaces

If your team currently investigates a suspicious IP, domain, email, or file indicator like this:

```
Open VirusTotal → copy results → Open Shodan → copy results
→ Open AbuseIPDB → copy results → Open OTX → copy results
→ Paste into spreadsheet → manually decide if it's actually a threat
→ Write up findings for the team
```

...every investigation costs **30–90 minutes of analyst time**, depends on whoever's doing it remembering to check every source, and still ends with a judgment call rather than a quantified answer.

**With SAYANJALI OSINT:**

```bash
python main.py -q suspicious-domain.com -f pdf
```

One command. Every source queried. Cross-correlated against a built-in reputation database. Risk-scored. Verdict delivered. Report generated.

| What you're paying for today | What SAYANJALI OSINT gives back |
|---|---|
| Analyst hours spent tab-switching | Minutes per investigation |
| Inconsistent investigation quality (depends who's doing it) | Standardized, repeatable methodology every time |
| No audit trail | PDF / HTML / JSON reports for every investigation |
| Manual judgment calls on ambiguous indicators | Automated Risk Score + Threat Verdict + Confidence Level |
| Re-querying the same indicator repeatedly | Local cache — instant results on repeat lookups |

---

## 🎯 Who This Is Built For

**Security Operations Centers (SOC)** — standardize triage across your whole analyst team so investigation quality doesn't depend on tenure or who's on shift.

**Independent security consultants & freelancers** — deliver client-ready PDF threat reports without building your own tooling or paying for five separate API subscriptions plus the time to stitch them together.

**Penetration testers & red teams** — passive reconnaissance that builds a target profile without sending a single packet at the target.

**Digital investigators & OSINT analysts** — correlate indicators across identity, infrastructure, and reputation data in one workflow instead of five.

**Threat intelligence teams** — feed JSON output directly into your existing SIEM or ticketing pipeline.

---

## 🧠 What You Get

### Domain & IP Intelligence
WHOIS, DNS enumeration, ASN identification, subdomain discovery, reverse DNS, and geolocation — for both domains and IP addresses, in one query.

```bash
python main.py -q google.com
python main.py -q 8.8.8.8
```

### Geolocation Intelligence
Forward geocoding, reverse geocoding, and nearby place discovery, useful for physical-location context in investigations.

```bash
python main.py -q "Hyderabad, India"
python main.py -q "17.3850,78.4867"
```

### Four Threat Intelligence Sources, One Query

| Source | What it adds to your verdict |
|---|---|
| **VirusTotal** | Malicious / suspicious / harmless detection counts from 70+ engines |
| **Shodan** | Exposed ports, services, and host fingerprinting |
| **AbuseIPDB** | Abuse confidence score and historical abuse reports |
| **AlienVault OTX** | Community threat pulse correlation |

### The Part That Actually Saves You Time: Automated Correlation

This is the difference between a data aggregator and a decision-support tool.

**IOC Risk Engine** — takes everything gathered above and produces a single Risk Score, Risk Classification, and Threat Verdict. No more eyeballing four different dashboards and guessing.

**Threat Feed Correlation Engine** — checks every indicator against a built-in reputation database of known malicious IPs, domains, emails, and URLs, and returns a Correlation Verdict.

**Sentinel Intelligence Layer** — the v2.1 addition that fuses all of the above into one coherent assessment, so the output you read is a conclusion, not a data dump.

### Identity & Email Intelligence
SPF/DMARC detection for email domains, plus username footprint checks across GitHub, GitLab, Reddit, DockerHub, Medium, HackerOne, and Keybase — useful for verifying whether an identity behind an indicator is consistent or fabricated.

### Reports You Can Actually Hand to Someone
```bash
python main.py -q target.com -f pdf    # Client/executive-ready report
python main.py -q target.com -f html   # Interactive shareable dashboard
python main.py -q target.com -f json   # Pipe into your SIEM or ticketing system
```

### Built to Run Anywhere Your Team Already Works
Linux, macOS, Windows, and Termux on Android — so field investigators aren't tied to a desktop.

---

## ⚙️ How It Works

```
   Your Query                Intelligence Layer              Output
┌──────────────┐         ┌────────────────────────┐      ┌──────────────┐
│  Domain / IP  │   →     │  VirusTotal · Shodan    │  →   │  Risk Score   │
│  Email / URL  │         │  AbuseIPDB · OTX        │      │  Verdict      │
│  Username     │         │  IOC Risk Engine        │      │  Confidence   │
│  Location     │         │  Threat Correlation     │      │  PDF/HTML/JSON│
└──────────────┘         └────────────────────────┘      └──────────────┘
                                     ↓
                          Local cache — instant on repeat
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/SHalimoosavi/sayanjali-osint.git
cd sayanjali-osint

pip install -r requirements.txt
python main.py --setup
```

Connect your own free-tier API keys for VirusTotal, Shodan, AbuseIPDB, and AlienVault OTX in `config.py`, and you're running investigations within minutes. The platform works with partial keys — add more over time as your correlation needs grow.

Full technical setup, command reference, and architecture documentation is available in the project [README](README.md).

---

## 📊 Current Release

| | |
|---|---|
| **Product** | SAYANJALI OSINT |
| **Release** | v2.1 — Sentinel Intelligence |
| **Status** | Stable |
| **Built By** | SAYANJALI NEXUS PRIVATE LIMITED |

---

## 🏢 Part of a Broader Platform Suite

SAYANJALI OSINT is built and maintained by **SAYANJALI NEXUS PRIVATE LIMITED**, a technology company building across AI, SaaS, cybersecurity, and blockchain. If your team needs adjacent tooling, ask about:

| Product | What it does |
|---|---|
| **SYJ ONE** | All-in-one productivity, dev, and security platform for Termux |
| **termux-pro** | Android-based development and security lab environment |
| **NexusRank AI** | Enterprise SEO/GEO intelligence SaaS |

---

## 📞 Get Started

<div align="center">

**Want a walkthrough, a custom deployment, or to discuss licensing for your team?**

### Syed Ali Hasan Moosavi
Founder — SAYANJALI NEXUS PRIVATE LIMITED

[![GitHub](https://img.shields.io/badge/GitHub-SHalimoosavi-181717?style=for-the-badge&logo=github)](https://github.com/SHalimoosavi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077b5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/syed-ali-hasan-moosavi-237734378/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-f97316?style=for-the-badge&logo=firefox&logoColor=white)](https://shalimoosavi.github.io/moosavi/)
[![X](https://img.shields.io/badge/X-@SHAliMoosavi-000000?style=for-the-badge&logo=x)](https://x.com/SHAliMoosavi)

📍 Hyderabad, India

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1a1f2e,100:0d1117&height=100&section=footer" width="100%"/>

**SAYANJALI OSINT v2.1 — Sentinel Intelligence**

*Intelligence. Visibility. Correlation.*

</div>
