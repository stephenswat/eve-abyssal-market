#!/bin/bash

poetry run python -Wd manage.py migrate --noinput
poetry run python -Wd manage.py collectstatic --noinput
