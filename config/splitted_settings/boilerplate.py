from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0hsf(im%p0x)uy_j(ky)4tnfsbi^$sm9(0(ksz@+q7x)gyvye$'

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'
