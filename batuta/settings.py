from pathlib import Path
import os
from .theam_setting import JAZZMIN_SETTINGS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def load_env():
    env_file = os.path.join(BASE_DIR, '.env')
    if os.path.exists(env_file):
        with open(env_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split('=')
                    os.environ[key] = value

# Load environment variables from the .env file
load_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(8oiyl-#)(d3@#uu$6g=!+g8lglz@6-fo&up+q%+0q^m16s3@-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'account.CustomUser'
SITE_OWNER_EMAIL = '14ing.dev@gmail.com'


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about',
    'account',
    'blog',
    'contact',
    'company_setting',
    'home',
    'shop',
    'rest_framework',
    'rest_framework.authtoken',
    "django_filters",
    'drf_yasg',
    'core',
    'djoser',
    "corsheaders",
    'django_seed',
    'ckeditor',
    'ckeditor_uploader'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = 'batuta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = 'batuta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv('TIME_ZONE')

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = os.getenv('STATIC_URL')
STATICFILES_DIRS = [os.path.join(BASE_DIR, str(os.getenv('STATICFILES_DIRS')))]
STATIC_ROOT = os.path.join(BASE_DIR, str(os.getenv('STATIC_ROOT')))
MEDIA_URL = str(os.getenv('MEDIA_URL'))
MEDIA_ROOT = os.path.join(BASE_DIR, str(os.getenv('MEDIA_ROOT')))
STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

CKEDITOR_UPLOAD_PATH = "uploads/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEVELOPER_EMAIL = '14ing.dev@gmail.com'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend','rest_framework.filters.SearchFilter'],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
}



# Allow all origins (not recommended for production)
CORS_ALLOW_ALL_ORIGINS = True

# OR specify allowed origins
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://apitest.genfourtech.com",
    "https://www.apitest.genfourtech.com",
    "https://admin.batutapositiva.com",
    "https://www.admin.batutapositiva.com",
    
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'iamamirkusi@gmail.com'
EMAIL_HOST_PASSWORD = 'ihrd cxsi stxu fbrw'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_REPLY_TO_EMAIL = EMAIL_HOST_USER
COMPANY_EMAIL = '`14ing.dev@gmail.com'

# SWAGGER_SETTINGS={

#       'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header'
#       }
#    }

#JAZZMIN SETTING
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
