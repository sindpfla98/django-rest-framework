from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'birdview_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'PORT': '',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}