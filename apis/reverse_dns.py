import socket


def reverse_dns_lookup(ip: str) -> dict:

    try:

        hostname, aliases, addresses = socket.gethostbyaddr(ip)

        return {
            "hostname": hostname,
            "aliases": aliases,
            "addresses": addresses
        }

    except Exception as e:

        return {
            "error": str(e)
        }
