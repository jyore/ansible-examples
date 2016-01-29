from __future__ import unicode_literals
import os

SECRET_KEY = os.environment.get("SECRET_KEY","")
NEVERCACHE_KEY = os.environment.get("NEVERCACHE	_KEY","")
ALLOWED_HOSTS = os.environment.get("ALLOWED_HOSTS","")


DATABASES = {
	"default" : {
		"ENGINE" : "django.db.backends.postgresql_psycopg2",
		"NAME" : os.environ.get("DATABASE_NAME",""),
		"USER" : os.environ.get("DATABASE_USER",""),
		"PASSWORD" : os.environ.get("DATABASE_PASSWORD",""),
		"HOST" : os.environ.get("DATABASE_HOST",""),
		"PORT" : os.environ.get("DATABASE_PORT","")
	}
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "mezzanine"

CACHES = {
	"default" : {
		"BACKEND" : "django.core.cache.backends.memcached.MemcachedCache",
		"LOCATION" : os.environ.get("MEMCACHED_LOCATION", "memcached:11211")
	}
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

TWITTER_ACCESS_TOKEN_KEY = os.environ.get("TWITTER_ACCESS_TOKEN_KEY","")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET","")
TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY","")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET","")
TWITTER_DEFAULT_QUERY = "from:ansible"
