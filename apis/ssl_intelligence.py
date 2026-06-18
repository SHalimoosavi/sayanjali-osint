import ssl
import socket
from datetime import datetime


def ssl_intelligence(domain: str) -> dict:

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain, 443),
            timeout=10
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

                issuer = dict(
                    x[0] for x in cert["issuer"]
                )

                subject = dict(
                    x[0] for x in cert["subject"]
                )

                expires = datetime.strptime(
                    cert["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_left = (
                    expires - datetime.utcnow()
                ).days

                return {
                    "issuer": issuer.get(
                        "organizationName"
                    ),
                    "common_name": subject.get(
                        "commonName"
                    ),
                    "expires": expires.isoformat(),
                    "days_remaining": days_left,
                    "tls_version": ssock.version(),
                    "valid": days_left > 0
                }

    except Exception as e:

        return {
            "error": str(e)
        }
