#!/usr/bin/env sh

# geokinesia
# scripts/dokku/celery/worker.sh

set -eux; \

newrelic-admin run-program celery -A config worker -E
