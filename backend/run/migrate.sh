#!/bin/bash

set -e
set -o pipefail
set -u

poetry run python -Wd manage.py migrate --noinput
poetry run python -Wd manage.py collectstatic --noinput
