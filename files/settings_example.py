from files.base_settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your database name',
        'USER': 'your postgre user',
        'PASSWORD': 'your password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}