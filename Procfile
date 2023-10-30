web: gunicorn config.wsgi:application --workers 3 --threads 2 --timeout 200
worker: celery -A config worker --beat -l info
flower: celery -A config flower --basic-auth=owidah:datalab
