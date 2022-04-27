# visual-perception-quiz

## Setup

Create PostgreSQL database and user:

```
sudo -u postgres psql
postgres=# CREATE DATABASE quiz;
postgres=# CREATE USER <user> WITH PASSWORD <password>;
postgres=# ALTER ROLE <user> SET client_encoding TO 'utf8';
postgres=# ALTER ROLE <user> SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE <user> SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE quiz TO <user>;
postgres=# \q
```

Update the database configuration in `mysite/settings/dev.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiz',
        'USER': '<user>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Set an enviroment variable for the Django settings module:

```
export DJANGO_SETTINGS_MODULE='mysite.settings.dev'
```

Install Python dependencies:

```
$ pip install -r requirements.txt
```

Quiz setup::

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py create_questions
python manage.py apply_image_numbers
python manage.py generate_percentages
python manage.py apply_correct
```

Check 83 questions were created:

```
python manage.py count_questions  # should print 83
```

Start the Django development server (will run on port 8000 by default):

```
python manage.py runserver
```

Visit `localhost:8000` in web browser.