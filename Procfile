web: gunicorn config.wsgi:application
release: python manage.py migrate && python -c "import nltk;nltk.download('vader_lexicon')"
#worker: celery -A config worker --loglevel=INFO
#beat: celery -A config beat --loglevel=INFO
