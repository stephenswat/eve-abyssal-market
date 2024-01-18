#!/bin/bash

set -e
set -o pipefail
set -u

poetry run python -Wd manage.py migrate --noinput
# poetry run python -Wd manage.py sde_get_items
# poetry run python -Wd manage.py sde_get_map
# poetry run python -Wd manage.py get_abyssal_types
poetry run python -Wd manage.py collectstatic --noinput
