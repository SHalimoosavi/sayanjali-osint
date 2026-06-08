def format_html(report: dict) -> str:
    lat = report.get("latitude", 0)
    lon = report.get("longitude", 0)
    has_map = lat != 0 and lon != 0
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>SAYANJALI OSINT Report</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>body{{font-family:Arial; margin:20px;}} #map{{height:400px; width:100%; margin-top:20px;}}</style>
</head>
<body>
    <h1>🔍 SAYANJALI OSINT Report</h1>
    <p><b>Query:</b> {report.get('query')} ({report.get('query_type')})</p>
    <p><b>Processing Time:</b> {report.get('processing_time_seconds')}s</p>
    <pre style="background:#f4f4f4; padding:10px;">{str(report)}</pre>
    {"<div id='map'></div><script src='https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'></script><script>var map=L.map('map').setView(["+str(lat)+","+str(lon)+"], 13); L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map); L.marker(["+str(lat)+","+str(lon)+"]).addTo(map);</script>" if has_map else ""}
</body>
</html>"""
    return html
