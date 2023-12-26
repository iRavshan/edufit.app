import os
import dotenv
from pathlib import Path
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'R$2aL9p!Qs6w#8h*3vF5nU7tG@4i%Y0oR$2aL9p!Qs6w#8h*3vF5nU7tG@4i%Y0o'

DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://edufit.uz']

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 518400
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'user',
    'rating',
    'competition',
    'ckeditor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'g16GFE1AD63DCEa*1**d*4fCD-12dGgD',
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT': '30512'
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'user.CustomUser'

LOGIN_URL = reverse_lazy('login')

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('uz', _('Uzbek')),
    ('en', _('English')),
    ('ru', _('Russian'))
)

LANGUAGE_CODE = 'uz'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

PARLER_LANGUAGES = {
    None: (
        {'code': 'uz',}, 
        {'code': 'en',}, 
        {'code': 'ru',}, 
    ),
    'default': {
        'fallbacks': ['uz'],
        'hide_untranslated': False,
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'