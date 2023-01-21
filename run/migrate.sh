#!/bin/bash

poetry run python manage.py migrate --noinput
poetry run python manage.py collectstatic --noinput
