import json


def format_html(report: dict) -> str:

    ai = report.get("ai_summary", {})
    asn = report.get("asn_info", {})
    vt = report.get("virustotal", {})
    shodan = report.get("shodan", {})
    abuse = report.get("abuseipdb", {})
    otx = report.get("otx", {})

    html = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="utf-8">

<title>SAYANJALI OSINT Dashboard</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background: #0f172a;
    color: white;
    padding: 20px;
}}

h1 {{
    text-align: center;
}}

.grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(320px,1fr));
    gap: 20px;
}}

.card {{
    background: #1e293b;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.4);
}}

.card h2 {{
    margin-top: 0;
    color: #38bdf8;
}}

pre {{
    white-space: pre-wrap;
    word-wrap: break-word;
}}

</style>

</head>

<body>

<h1>SAYANJALI OSINT Dashboard</h1>

<div class="grid">

<div class="card">
<h2>Executive Summary</h2>
<p><b>Risk Score:</b> {ai.get("risk_score","N/A")}</p>
<p><b>Verdict:</b> {ai.get("verdict","N/A")}</p>
<p><b>Confidence:</b> {ai.get("confidence","N/A")}</p>

<ul>
{''.join(f'<li>{x}</li>' for x in ai.get("findings", []))}
</ul>

</div>

<div class="card">
<h2>ASN Intelligence</h2>
<pre>{json.dumps(asn, indent=2)}</pre>
</div>

<div class="card">
<h2>VirusTotal Intelligence</h2>
<pre>{json.dumps(vt, indent=2)}</pre>
</div>

<div class="card">
<h2>Shodan Intelligence</h2>
<pre>{json.dumps(shodan, indent=2)}</pre>
</div>

<div class="card">
<h2>AbuseIPDB Intelligence</h2>
<pre>{json.dumps(abuse, indent=2)}</pre>
</div>

<div class="card">
<h2>AlienVault OTX</h2>
<pre>{json.dumps(otx, indent=2)}</pre>
</div>

<div class="card">
<h2>Metadata</h2>

<p><b>Query:</b> {report.get("query")}</p>

<p><b>Type:</b> {report.get("query_type")}</p>

<p><b>Processing Time:</b>
{report.get("processing_time_seconds")}s</p>

<p><b>Cache:</b>
{report.get("cache_status","N/A")}</p>

</div>

</div>

</body>
</html>
"""

    return html
