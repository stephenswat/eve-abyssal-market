#!/bin/bash

set -e
set -o pipefail
set -u

poetry run python manage.py run_huey -w ${CONSUMER_COUNT} -f
