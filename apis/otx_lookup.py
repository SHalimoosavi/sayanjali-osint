import os
import requests

from dotenv import load_dotenv

load_dotenv()


def lookup_otx(indicator: str, indicator_type: str) -> dict:

    api_key = os.getenv("OTX_API_KEY")

    if not api_key:
        return {
            "error": "OTX_API_KEY not configured"
        }

    try:

        indicator_type = indicator_type.lower()

        if indicator_type == "domain":

            url = (
                "https://otx.alienvault.com/api/v1/"
                f"indicators/domain/{indicator}/general"
            )

        elif indicator_type == "ip":

            url = (
                "https://otx.alienvault.com/api/v1/"
                f"indicators/IPv4/{indicator}/general"
            )

        else:

            return {
                "error": "Unsupported indicator type"
            }

        response = requests.get(
            url,
            headers={
                "X-OTX-API-KEY": api_key
            },
            timeout=30
        )

        if response.status_code != 200:

            return {
                "error": f"HTTP {response.status_code}"
            }

        data = response.json()

        pulse_info = data.get(
            "pulse_info",
            {}
        )

        return {
            "indicator": indicator,
            "indicator_type": indicator_type,
            "reputation": data.get(
                "reputation",
                0
            ),
            "pulse_count": pulse_info.get(
                "count",
                0
            ),
            "country": data.get(
                "country_code"
            ),
            "asn": data.get(
                "asn"
            ),
            "city": data.get(
                "city"
            )
        }

    except requests.exceptions.Timeout:

        return {
            "warning": "OTX timeout"
        }

    except Exception as e:

        return {
            "error": str(e)
        }
