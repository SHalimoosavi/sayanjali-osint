import os
import requests

from dotenv import load_dotenv

load_dotenv()


def lookup_abuseipdb(ip: str) -> dict:

    api_key = os.getenv(
        "ABUSEIPDB_API_KEY"
    )

    if not api_key:

        return {
            "error": "ABUSEIPDB_API_KEY not configured"
        }

    try:

        response = requests.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers={
                "Key": api_key,
                "Accept": "application/json"
            },
            params={
                "ipAddress": ip,
                "maxAgeInDays": 90,
                "verbose": True
            },
            timeout=15
        )

        if response.status_code != 200:

            return {
                "error": f"HTTP {response.status_code}",
                "details": response.text
            }

        data = response.json().get(
            "data",
            {}
        )

        return {
            "ip": data.get("ipAddress"),
            "abuse_score": data.get(
                "abuseConfidenceScore",
                0
            ),
            "country": data.get(
                "countryCode"
            ),
            "isp": data.get(
                "isp"
            ),
            "domain": data.get(
                "domain"
            ),
            "usage_type": data.get(
                "usageType"
            ),
            "total_reports": data.get(
                "totalReports",
                0
            ),
            "last_reported": data.get(
                "lastReportedAt"
            )
        }

    except Exception as e:

        return {
            "error": str(e)
        }
