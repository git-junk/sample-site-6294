from pathlib import Path
import os

SECRET_KEY = 'django-insecure-!t97nj@_5r4io+f3l&(o9-!f=bmes$7y%#n^$4q4ezx952czjj'

#settings.pyからそのままコピー
BASE_DIR = Path(__file__).resolve().parent.parent

#settings.pyからそのままコピー
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sample_site_db',
        'USER': 'postgres',
        'PASSWORD': 'possql0701',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DEBUG = True #ローカルでDebugできるようになります
