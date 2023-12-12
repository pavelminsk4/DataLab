web: gunicorn config.wsgi:application --workers 3 --threads 9 --timeout 120
worker: celery -A config worker --beat -l fatal
flower: celery -A config flower --url_prefix=flower
release: python manage.py collectstatic --noinput --ignore node_modules --ignore frontend --ignore venv
