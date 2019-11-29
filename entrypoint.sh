#!/bin/bash
set -e

cd /app
if [[ "$1" = 'dbmigrate' ]]; then
    python manage.py migrate
fi
if [[ "$1" = 'web' ]]; then
    gunicorn --bind 0.0.0.0:3000 biotower.wsgi
fi
if [[ -z "$1" ]]; then
    echo "No args. ($@)"
    exit 1
fi
