import re
import socket
from typing import Tuple, Literal
from ipaddress import IPv4Address, IPv6Address, AddressValueError

def is_valid_ip(value: str) -> bool:
    try:
        IPv4Address(value) or IPv6Address(value)
        return True
    except AddressValueError:
        return False

def is_valid_domain(value: str) -> bool:
    pattern = r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$'
    return bool(re.match(pattern, value.lower()))

def is_valid_coordinates(lat: float, lon: float) -> bool:
    return -90 <= lat <= 90 and -180 <= lon <= 180

def detect_query_type(query: str) -> Tuple[Literal["ip", "domain", "address", "coordinates"], str]:
    query = query.strip()
    coord_pattern = r'^(-?\d+\.?\d*)\s*,\s*(-?\d+\.?\d*)$'
    coord_match = re.match(coord_pattern, query)
    if coord_match:
        lat, lon = float(coord_match.group(1)), float(coord_match.group(2))
        if is_valid_coordinates(lat, lon):
            return ("coordinates", f"{lat},{lon}")
    if is_valid_ip(query):
        return ("ip", query)
    if is_valid_domain(query):
        return ("domain", query.lower())
    return ("address", query)

def resolve_domain_to_ip(domain: str) -> str:
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as e:
        raise ValueError(f"Failed to resolve domain '{domain}': {e}")
