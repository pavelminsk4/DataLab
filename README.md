# Installing the project

1. Comment out requirement aspose-words (on Mac)
2. Install Django: pip3 install -r requirements.txt
3. Copy .env.example to .env
4. Adjust DATABASE_URL in the .env file to match local Postgres user
5. Create an empty database in Postgres called anova_dev (`psql -d postgres` then `CREATE DATABASE anova_dev;`)
6. Run migrations via `python3 manage.py migrate`

# Running tests

**Backend**
1. `cd frontend`
2. `nvm install 18` (make sure you have nvm installed)
3. `yarn` (to install JS libraries)
4. `yarn serve`
5. `python3 manage.py test`

**Celery**
1. `brew install redis`
2. `brew services start redis`
3. `celery -A config worker --beat -l info`
4. `celery -A config flower --url_prefix=flower` (for monitoring)

**Frontend**
1. `cd frontend`
2. `yarn` (to install JS libraries)
3. `yarn test`

# Running the developer's environment

1. `python3 manage.py createsuperuser`
2. `yarn serve` (to run the frontend)
3. `python3 manage.py runserver`
