web: gunicorn config.wsgi:application --timeout 200
release: python manage.py migrate
worker: celery -A config worker --beat -l info
