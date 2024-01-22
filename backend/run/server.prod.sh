#!/bin/bash

set -e
set -o pipefail
set -u

poetry run gunicorn --workers 16 --bind 0.0.0.0:8000 abyssal_market.wsgi:application
