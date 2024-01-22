#!/bin/bash

set -e
set -o pipefail
set -u

poetry run python -Wd manage.py runserver 0.0.0.0:8000
