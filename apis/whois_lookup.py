import whois
from datetime import datetime

def safe_date(value):
    if isinstance(value, list):
        value = value[0]

    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")

    return str(value) if value else "N/A"


def lookup_whois(domain: str) -> dict:
    try:
        data = whois.whois(domain)

        return {
            "domain": domain,
            "registrar": str(data.registrar) if data.registrar else "N/A",
            "creation_date": safe_date(data.creation_date),
            "expiration_date": safe_date(data.expiration_date),
            "updated_date": safe_date(data.updated_date),
            "name_servers": (
                list(data.name_servers)
                if data.name_servers
                else []
            ),
            "status": (
                list(data.status)
                if isinstance(data.status, list)
                else [str(data.status)]
                if data.status
                else []
            )
        }

    except Exception as e:
        return {
            "domain": domain,
            "error": str(e)
        }
