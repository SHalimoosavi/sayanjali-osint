from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class Location(BaseModel):
    latitude: float
    longitude: float
    accuracy_radius_km: Optional[float] = None
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)

class GeoIPResult(BaseModel):
    ip: str
    country: str
    country_code: str
    region: Optional[str] = None
    city: Optional[str] = None
    location: Location
    isp: Optional[str] = None
    organization: Optional[str] = None
    timezone: Optional[str] = None
    confidence: float

class Address(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None
    country: str
    country_code: str
    full_address: str
    confidence: float

class ReverseGeocodeResult(BaseModel):
    location: Location
    address: Address
    place_name: Optional[str] = None
    place_type: Optional[str] = None

class ForwardGeocodeResult(BaseModel):
    query: str
    location: Location
    address: Address
    place_type: Optional[str] = None

class PlaceResult(BaseModel):
    name: str
    location: Location
    address: Address
    place_type: str
    distance_meters: Optional[float] = None

class PlaceSearchResult(BaseModel):
    query: str
    place_type: str
    radius_meters: float
    results: List[PlaceResult]
    total_results: int

class DomainResult(BaseModel):
    domain: str
    primary_ip: str
    all_ips: List[str]
    geolocation: Optional[GeoIPResult] = None

class OSINTReport(BaseModel):
    query: str
    query_type: str
    timestamp: datetime
    ip_geolocation: Optional[GeoIPResult] = None
    reverse_geocode: Optional[ReverseGeocodeResult] = None
    forward_geocode: Optional[ForwardGeocodeResult] = None
    nearby_places: Optional[PlaceSearchResult] = None
    domain_info: Optional[DomainResult] = None
    processing_time_seconds: float
    sources_queried: List[str]
    confidence_score: float
    errors: List[str] = []
