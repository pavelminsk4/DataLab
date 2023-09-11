web: gunicorn config.wsgi:application --workers 3 --threads 2 --timeout 200
release: python manage.py migrate
worker: celery -A config worker --beat -l info
