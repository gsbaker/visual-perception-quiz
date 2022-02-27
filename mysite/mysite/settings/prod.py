from mysite.settings.base import *
import os

# Override base settings here

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY'] 

ALLOWED_HOSTS = ['40.71.223.198', 'www.visualperceptionquiz.com', 'https://www.visualperceptionquiz.com', 'visualperceptionquiz.com', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiz',
        'USER': 'george',
        'PASSWORD': 'django1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
