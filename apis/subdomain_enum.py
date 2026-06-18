import requests


def enumerate_subdomains(domain: str) -> dict:
    """
    Fast subdomain enumeration.

    Phase 17 Optimization:
    - Reduced timeout
    - Limits crt.sh response size
    - Gracefully handles failures
    - Prevents slow scans from blocking investigations
    """

    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"

        response = requests.get(
            url,
            timeout=5
        )

        if response.status_code != 200:
            return {
                "count": 0,
                "results": [],
                "source": "crt.sh",
                "status": f"HTTP {response.status_code}"
            }

        try:
            data = response.json()

        except Exception:
            return {
                "count": 0,
                "results": [],
                "source": "crt.sh",
                "status": "invalid_json"
            }

        if not isinstance(data, list):
            return {
                "count": 0,
                "results": [],
                "source": "crt.sh",
                "status": "unexpected_response"
            }

        results = set()

        # Limit processing for performance
        for item in data[:200]:

            name_value = str(
                item.get(
                    "name_value",
                    ""
                )
            )

            for subdomain in name_value.split("\n"):

                subdomain = (
                    subdomain
                    .strip()
                    .lower()
                )

                if (
                    subdomain
                    and not subdomain.startswith("*.")
                    and subdomain.endswith(domain.lower())
                ):
                    results.add(subdomain)

        return {
            "count": len(results),
            "results": sorted(results),
            "source": "crt.sh",
            "status": "success"
        }

    except requests.exceptions.Timeout:

        return {
            "count": 0,
            "results": [],
            "source": "crt.sh",
            "status": "timeout"
        }

    except Exception as e:

        return {
            "count": 0,
            "results": [],
            "source": "crt.sh",
            "status": f"error: {str(e)}"
        }
