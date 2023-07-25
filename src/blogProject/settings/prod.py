from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tomimartinez28$default',
        'USER': 'tomimartinez28',
        'PASSWORD': 'abcdefgh123',
        'HOST': 'tomimartinez28.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
} 