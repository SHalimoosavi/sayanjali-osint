import requests


def enumerate_subdomains(domain: str) -> dict:

    results = set()

    try:

        url = (
            "https://crt.sh/"
            f"?q=%.{domain}&output=json"
        )

        response = requests.get(
            url,
            timeout=30
        )

        if response.status_code == 200:

            try:

                data = response.json()

                for item in data:

                    name = item.get(
                        "name_value",
                        ""
                    )

                    for sub in name.split("\n"):

                        sub = sub.strip().lower()

                        if (
                            sub
                            and "*." not in sub
                            and domain in sub
                        ):
                            results.add(sub)

            except Exception:
                pass

    except Exception:
        pass

    return {
        "count": len(results),
        "results": sorted(
            list(results)
        )
    }
