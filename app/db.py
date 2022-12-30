from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

POSTGRESQL={
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'db',
        'USER':'postgres',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'5432'

    }
}