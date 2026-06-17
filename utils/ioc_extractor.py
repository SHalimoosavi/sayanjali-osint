import re


IP_REGEX = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

DOMAIN_REGEX = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"

EMAIL_REGEX = (
    r"\b[a-zA-Z0-9._%+-]+@"
    r"[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
)

URL_REGEX = r"https?://[^\s]+"


def extract_iocs(text: str) -> dict:

    return {
        "ips": sorted(
            list(
                set(
                    re.findall(
                        IP_REGEX,
                        text
                    )
                )
            )
        ),
        "domains": sorted(
            list(
                set(
                    re.findall(
                        DOMAIN_REGEX,
                        text
                    )
                )
            )
        ),
        "emails": sorted(
            list(
                set(
                    re.findall(
                        EMAIL_REGEX,
                        text
                    )
                )
            )
        ),
        "urls": sorted(
            list(
                set(
                    re.findall(
                        URL_REGEX,
                        text
                    )
                )
            )
        )
    }
