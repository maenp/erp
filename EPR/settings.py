"""
Django settings for EPR project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i=v+^fto_s&cy9t%x9h!)iowd9l#d0c&1$let3g9xrp7fo2+rl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#指定自定义用户模型所在位置 是为了让Django用户认证系统使用我们自定义的用户模型
AUTH_USER_MODEL='userApp.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',#配置跨域
    'userApp',
    'csmApp',
    # 'App',
    # 'App2',
    # 'App3',
]
# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #跨域配置 放最前面
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',# 防止csrf攻击用的 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 根路由位置
ROOT_URLCONF = 'EPR.urls'
# 模板配置
# TEMPLATES = [
    # {
    #     'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #     'DIRS': [os.path.join(BASE_DIR,'templates')],
    #     'APP_DIRS': True,
    #     'OPTIONS': {
    #         'context_processors': [
    #             'django.template.context_processors.debug',
    #             'django.template.context_processors.request',
    #             'django.contrib.auth.context_processors.auth',
    #             'django.contrib.messages.context_processors.messages',
    #         ],
    #     },
    # },
# ]
TEMPLATES = [
    { #django 模板配置
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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
    { #jinja2 模板配置
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR,'jinja2_templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'environment':'EPR.jinja2_env.environment',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 项目入口
WSGI_APPLICATION = 'EPR.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'epr',                      #数据库名
        'HOST': 'cdb-0yodpccg.cd.tencentcdb.com',#主机地址
        'USER':'root',                           #用户名
        'PASSWORD':'mm5202000',                  #密码
        'PORT':10048                             #端口
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# 授权
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# 语言
# Lib\site-packages\django\conf\locale
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'
# 时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 是否使用国际标准时间 改为false 数据库存储时间与当地时间一致
USE_TZ = False 


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# 静态资源目录
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')  #
]

#跨域配置··················································                      

#如果为True，则将允许将cookie包含在跨站点HTTP请求中。默认为False
CORS_ALLOW_CREDENTIALS = True

#添加允许执行跨站点请求的主机 如果为True，则将不使用白名单，并且将接受所有来源。默认为False
# CORS_ORIGIN_ALLOW_ALL = True

#授权进行跨站点HTTP请求的来源列表(白名单)。默认为[]
CORS_ORIGIN_WHITELIST =[
    "https://example.com",
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]
#实际请求所允许的HTTP动词列表。
CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
	'VIEW',
)
#发出实际请求时可以使用的非标准HTTP标头的列表。
CORS_ALLOW_HEADERS = (
	'XMLHttpRequest',
	'X_FILENAME',
	'accept-encoding',
	'authorization',
	'content-type',
	'dnt',
	'origin',
	'user-agent',
	'x-csrftoken',
	'x-requested-with',
	'Pragma',
)
#··················································