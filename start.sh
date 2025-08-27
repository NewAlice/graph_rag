#! /usr/bin/env sh
set -e

if [ -z "$WEB_CONCURRENCY" ]; then
    GUNICORN_WORKERS=3
else
    GUNICORN_WORKERS=$WEB_CONCURRENCY
fi

gunicorn --forwarded-allow-ips "*" -k "uvicorn.workers.UvicornWorker" "app.main:app" --bind "0.0.0.0:8080" --workers "$GUNICORN_WORKERS"