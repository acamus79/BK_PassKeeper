import psycopg2 
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        connection = psycopg2.connect(
            user=config('DB_USER', default='postgres'), 
            password=config('DB_PASSWORD', default='postgres'),
            host=config('DB_HOST', default='localhost'),
            port=config('DB_PORT', default='5432'),
            database=config('DB_NAME', default='postgres')
        )
        return connection
    except (Exception, DatabaseError) as error:
        print(error)
        raise error

