import os
import shodan
from dotenv import load_dotenv

load_dotenv()


def lookup_shodan(ip: str) -> dict:
    """
    Lookup IP in Shodan.
    """

    api_key = os.getenv("SHODAN_API_KEY")

    if not api_key:
        return {
            "error": "SHODAN_API_KEY not configured"
        }

    try:

        api = shodan.Shodan(api_key)

        host = api.host(ip)

        return {
            "ip": host.get("ip_str"),
            "organization": host.get("org"),
            "os": host.get("os"),
            "country": host.get("country_name"),
            "hostnames": host.get("hostnames", []),
            "ports": host.get("ports", []),
            "last_update": host.get("last_update")
        }

    except Exception as e:

        return {
            "error": str(e)
        }
