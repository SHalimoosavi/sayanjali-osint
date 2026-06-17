import requests


PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Keybase": "https://keybase.io/{}",
    "DockerHub": "https://hub.docker.com/u/{}",
    "Medium": "https://medium.com/@{}",
    "HackerOne": "https://hackerone.com/{}"
}


def username_lookup(username: str) -> dict:

    results = {}

    found_count = 0

    for platform, url_template in PLATFORMS.items():

        url = url_template.format(username)

        try:

            response = requests.get(
                url,
                timeout=10,
                allow_redirects=True,
                headers={
                    "User-Agent": "SAYANJALI-OSINT"
                }
            )

            exists = response.status_code == 200

            if exists:
                found_count += 1

            results[platform] = {
                "exists": exists,
                "url": url,
                "status_code": response.status_code
            }

        except Exception:

            results[platform] = {
                "exists": False,
                "url": url,
                "status_code": None
            }

    confidence = round(
        (found_count / len(PLATFORMS)) * 100,
        2
    )

    return {
        "username": username,
        "platforms_found": found_count,
        "confidence": confidence,
        "results": results
    }
