from files.base_settings import *
import dj_database_url


DATABASES = {'default': dj_database_url.config(default=os.environ["DATABASE_URL"])}
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
ALLOWED_HOSTS += [
    'fileshare-oz.herokuapp.com',
]
DEBUG = False

