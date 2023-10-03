# Installing the project

1. Comment out requirement aspose-words (on Mac)
2. Install Django: pip3 install -r requirements.txt
3. Copy .env.example to .env
4. Adjust DATABASE_URL in the .env file to match local Postgres user
5. Create an empty database in Postgres called anova_dev (`psql -d postgres` then `CREATE DATABASE anova_dev;`)
6. Comment the following:
   * File reports/classes/online_pdf.py lines 1 and 14
   * File reports/classes/social_pdf.py lines 1 and 14
   * File reports/services/pdf_handler.py - the whole file
7. Run migrations via `python3 manage.py migrate`

# Running tests

1. `cd frontend`
2. `nvm install 18` (make sure you have nvm installed)
3. `yarn` (to install JS libraries)
4. `yarn serve`
5. `python3 manage.py test`

# Running the developer's environment

1. `python3 manage.py createsuperuser`
2. `python3 manage.py runserver`
