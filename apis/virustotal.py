import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")


def lookup_virustotal(query: str, query_type: str) -> dict:

    if not API_KEY:
        return {
            "error": "VirusTotal API key not configured"
        }

    headers = {
        "x-apikey": API_KEY
    }

    try:

        if query_type == "domain":

            url = f"https://www.virustotal.com/api/v3/domains/{query}"

        elif query_type == "ip":

            url = f"https://www.virustotal.com/api/v3/ip_addresses/{query}"

        else:

            return {
                "error": "Unsupported query type"
            }

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        if response.status_code != 200:

            return {
                "error": f"VirusTotal HTTP {response.status_code}"
            }

        data = response.json()

        stats = data.get(
            "data",
            {}
        ).get(
            "attributes",
            {}
        ).get(
            "last_analysis_stats",
            {}
        )

        reputation = data.get(
            "data",
            {}
        ).get(
            "attributes",
            {}
        ).get(
            "reputation",
            0
        )

        return {
            "reputation": reputation,
            "harmless": stats.get("harmless", 0),
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "undetected": stats.get("undetected", 0)
        }

    except Exception as e:

        return {
            "error": str(e)
        }
