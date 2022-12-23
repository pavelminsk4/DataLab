# scripts/dokku/celery/beat.sh

set -eux; \

newrelic-admin run-program celery -A config beat
