from prometheus_client import Counter

COUNTER_MODULES_CREATED = Counter(
    'mutaplasmid_modules_created',
    'Number of modules created',
    ['type']
)
