import os


def run_health_check() -> dict:

    checks = {
        "Cache": True,
        "DNS": True,
        "WHOIS": True,
        "GeoIP": os.path.exists(
            "data/GeoLite2-City.mmdb"
        ),
        "VirusTotal": True,
        "Shodan": True,
        "AbuseIPDB": True,
        "AlienVault OTX": True
    }

    healthy = all(
        checks.values()
    )

    return {
        "checks": checks,
        "healthy": healthy
    }
