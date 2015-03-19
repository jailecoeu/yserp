#coding:utf-8
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'yusheng_erp',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Memcache
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#        'TIMEOUT': 24 * 60 * 60,
#        }
#}

# Redis
CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:4",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
            }
    }
}

BROKER_URL = 'redis://127.0.0.1:6379/4'

ALLOWED_HOSTS = ['erp.yuanda.com',]
#SESSION_COOKIE_DOMAIN = '192.168.1.218'
#SESSION_COOKIE_DOMAIN = '192.168.2.218'

#import settings
#apps = list(settings.INSTALLED_APPS)
#apps.append('kindeditor')
#INSTALLED_APPS = tuple(apps)