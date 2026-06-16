import requests


def lookup_asn(ip: str) -> dict:

    providers = [
        f"https://ipapi.co/{ip}/json/",
        f"http://ip-api.com/json/{ip}"
    ]

    for url in providers:

        try:

            response = requests.get(
                url,
                timeout=10
            )

            if response.status_code != 200:
                continue

            data = response.json()

            asn = (
                data.get("asn")
                or data.get("as")
                or "N/A"
            )

            organization = (
                data.get("org")
                or data.get("isp")
                or data.get("asname")
                or "N/A"
            )

            network = (
                data.get("network")
                or data.get("query")
                or ip
            )

            country = (
                data.get("country_name")
                or data.get("country")
                or "N/A"
            )

            return {
                "asn": str(asn),
                "organization": str(organization),
                "network": str(network),
                "country": str(country)
            }

        except Exception:
            continue

    return {
        "asn": "N/A",
        "organization": "N/A",
        "network": "N/A",
        "country": "N/A"
    }
