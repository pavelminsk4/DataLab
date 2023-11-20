from pathlib import Path
import os
import environ

DEBUG = False

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'django-insecure-#v!p9&1x##2u#yt)l=o5ihm(=!&(y(w4j5p-_mbm(k&bc1i!jw'

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

CSRF_TRUSTED_ORIGINS = ['https://*.datalab.net']

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'accounts.apps.AccountsConfig',
    'project.apps.ProjectConfig',
    'crispy_forms',
    'webpack_loader',
    'rest_framework',
    'api.apps.ApiConfig',
    'import_export',
    'workspace.apps.WorkspaceConfig',
    'django_celery_beat',
    'django_celery_results',
    'countries_plus',
    'widgets.apps.WidgetsConfig',
    'django.contrib.postgres',
    'reports.apps.ReportsConfig',
    'alerts.apps.AlertsConfig',
    'drf_yasg',
    'tweet_binder.apps.TweetBinderConfig',
    'project_social.apps.ProjectSocialConfig',
    'ml_components.apps.MlComponentsConfig',
    'account_analysis.apps.AccountAnalysisConfig',
    'drf_multitokenauth',
    'twenty_four_seven.apps.TwentyFourSevenConfig',
    'comparison.apps.ComparisonConfig',
    'query_counter',
    'phonenumber_field',
    'multilanguage.apps.MultilanguageConfig',
    'expert_filters.apps.ExpertFiltersConfig',
    'talkwalker.apps.TalkwalkerConfig',
    'revproxy',
    'django_extensions',
]

ASGI_APPLICATION = 'config.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.DisableCSRF',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {"default": env.db("DATABASE_URL")}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = env('SERVER_TIME_ZONE')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'collectstatic/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'


WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'STATS_FILE': BASE_DIR.joinpath('frontend', 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
    }
}

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_RESULT_BACKEND = "django-db"
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

ROLLBAR = {
    'access_token': 'c1b9edc11da34304902b6472355e4025',
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}
