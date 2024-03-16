import pymysql

from dotenv import load_dotenv
import os
load_dotenv()

try:
    connection = pymysql.connect(
    host = os.getenv('DB_HOST'),
    port = 3306,
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = 'ChatGPT_users',
    cursorclass=pymysql.cursors.DictCursor
    )
    
    print(f'Connected')

    try:
        with connection.cursor() as cursor:
            cursor.execute('SHOW DATABASES;')
            print(cursor.fetchall())
            pass


    except Exception as ex:
        print(ex)

    pass

except Exception as e:
    print('Connection failed')
    print(e)