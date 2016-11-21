"""
Django settings for sopds project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm4l1c#nq6*zs!c3ri4dg4(54_7bvrl5uintni6p20tijlaxv!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'opds_catalog',
    'sopds_web_backend',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',  
    #'opds_catalog.opds_middleware.BasicAuthMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sopds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sopds_web_backend.views.sopds_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'sopds.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {    
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'sopds',
#        'HOST': 'localhost',
#        'USER': 'sopds',
#        'PASSWORD' : 'sopds',
#        'OPTIONS' : {
#            'init_command': "SET default_storage_engine=MyISAM;\
#                             SET sql_mode='';"
#        }
#    }             
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }         
}    

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-US'
#LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'static'


#
# SIMPLE OPDS SETTINGS
#
SOPDS_ROOT_LIB = 'W:\\_Downloads\\_Lib.rus.ec - Официальная\\lib.rus.ec\\'
#SOPDS_ROOT_LIB = '/mnt/SATA1TB-1/КНИГИ/BOOKS/'
#SOPDS_ROOT_LIB = '/mnt/nfs/КНИГИ/BOOKS/'
#SOPDS_ROOT_LIB = os.path.join(BASE_DIR,'opds_catalog\\tests\\data\\')
#SOPDS_ROOT_LIB = "d:\\BOOKS\\"


SOPDS_AUTH = True
SOPDS_SCAN_SHED_MIN ='0'
SOPDS_SCAN_SHED_HOUR ='0,12'

SOPDS_SINGLE_COMMIT = True
SOPDS_INPX_TEST_ZIP = True

#Конвертеры EPUB и MOBI
#SOPDS_FB2TOEPUB = os.path.join(BASE_DIR,'convert/fb2toepub/unix_dist/fb2toepub')
#SOPDS_FB2TOEPUB = os.path.join(BASE_DIR,'convert/fb2conv/fb2epub')
#SOPDS_FB2TOMOBI = os.path.join(BASE_DIR,'convert/fb2conv/fb2mobi')
#SOPDS_FB2TOEPUB = os.path.join(BASE_DIR, 'convert\\fb2epub\\fb2epub.cmd' if sys.platform =='win32' else 'convert/fb2epub/fb2epub' )

