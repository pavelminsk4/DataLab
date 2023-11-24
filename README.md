# Installing the project

1. Install Django: pip3 install -r requirements.txt
2. Copy .env.example to .env
3. Adjust DATABASE_URL in the .env file to match local Postgres user
4. Create an empty database in Postgres called anova_dev (`psql -d postgres` then `CREATE DATABASE anova_dev;`)
5. Run migrations via `python3 manage.py migrate`

# Running tests

**Backend**
1. `nvm install 18` (make sure you have nvm installed)
2. `yarn` (to install JS libraries)
3. `yarn serve`
4. `python3 manage.py test`

**Celery**
1. `brew install redis`
2. `brew services start redis`
3. `celery -A config worker --beat -l info`
4. `celery -A config flower --url_prefix=flower` (for monitoring)

**Frontend**
1. `yarn` (to install JS libraries)
2. `yarn test`

# Running the developer's environment

1. `python3 manage.py createsuperuser`
2. `yarn serve` (to run the frontend)
3. `python3 manage.py runserver`

# Setting up a server to serve static files

1. `dokku storage:mount app /var/lib/dokku/data/storage/app/collectstatic:/app/collectstatic`
2. `location /static/ {alias /var/lib/dokku/data/storage/app/collectstatic/;}` (create static.conf file with this code)
