# -*- coding: utf-8 -*
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# M:\SMCC\mysite

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hfmtg)40tnizlk@63g-(36wu%un%v(65yrasac4wrm028jd5ve'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = ('M:/SMCC/mysite/Statics/templates',)
#template path setting




ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
    'signups',
    'products',
   # 'Statics',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

'''
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}
'''
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql', #添加数据库引擎；选项['postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'].
        'NAME': 'QM', # 数据库文件的路径.
        # The following settings are not used with sqlite3:
        # 下面的配置不适用于sqlite3:
        'USER': 'saxon',    # 数据库登陆用户名
        'PASSWORD': 'cccccc', # 数据库登陆密码
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP. # 主机名
        'PORT': '3306',                      # Set to empty string for default. # 端口号
    }
}








# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT =  'M:/SMCC/mysite/Statics/static-only/'#配置STATIC根目录,该目录可以通过py命令将所有app的static文件收集起来
STATIC_URL = '/static/'
#这里只是为了方便以后链接'static'就可以用文字STATIC_URL代替，
#并不是系统必须的某个设置


MEDIA_ROOT  =  'M:/SMCC/mysite/Statics/media/'



MEDIA_URL = '/media/'

STATICFILES_DIRS = ('M:/SMCC/mysite/Statics/static',)
# you can define a list of directories (STATICFILES_DIRS) 
# in your settings file where Django will also look for static files. 
# 静态文件链接列表 元组