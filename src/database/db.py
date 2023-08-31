import psycopg2 
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        connection = psycopg2.connect(
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('DB_HOST'),
            port=config('DB_PORT'),
            database=config('DB_NAME')
        )
        return connection
    except (Exception, DatabaseError) as error:
        print(error)
        raise error

