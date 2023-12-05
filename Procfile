web: gunicorn config.wsgi:application --workers 3 --threads 2 --timeout 200
worker: celery -A config worker --beat -l fatal --concurrency=1
flower: celery -A config flower --url_prefix=flower
release: python manage.py collectstatic --no-input
