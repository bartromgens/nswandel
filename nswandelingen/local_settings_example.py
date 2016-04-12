import os
APP_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: Make this unique, and don't share it with anybody.
SECRET_KEY = ''

TIME_ZONE = "Europe/Amsterdam"

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": os.path.join(APP_DIR, "dev.db"),
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# Static files (CSS, JavaScript, Images)

#STATIC_ROOT = '/home/username/webapps/rbbingo_static/'
STATIC_ROOT = ''

#STATIC_URL = 'http://www.domain.com/static/'
STATIC_URL = "/static/"

REGISTRATION_OPEN = True
