from prometheus_client import Counter

COUNTER_CONTRACTS_FOUND = Counter(
    "mutaplasmid_contracts_found", "Number of contracts found", ["region", "type"]
)

COUNTER_CONTRACTS_SCANNED = Counter(
    "mutaplasmid_contracts_scanned", "Number of contracts scanned", ["region", "type"]
)
