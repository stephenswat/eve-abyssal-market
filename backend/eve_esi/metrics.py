from prometheus_client import Counter

COUNTER_ESI_REQUESTS = Counter(
    "esi_requests", "Number of ESI requests", ["endpoint", "status"]
)
