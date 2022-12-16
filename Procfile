web: gunicorn config.wsgi:application
release: python manage.py migrate
#worker: celery -A config worker --loglevel=INFO
#beat: celery -A config beat --loglevel=INFO
