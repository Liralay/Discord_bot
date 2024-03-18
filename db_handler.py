import pymysql
from mysql.connector import Error

import logging
logger = logging.getLogger(__name__)



from dotenv import load_dotenv
import os
load_dotenv()


def create_connection():
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
        return connection
    except Error as e:
        print(f"Ошибка при подключении к MySQL: {e}")
        return None


def func(user_id):
    connection = create_connection()
    logger.info('Connected to DB')
    global max_q
    with connection.cursor() as cursor:
        logger.info('Executing SQL Q')
        cursor.execute('SELECT `uses` FROM `gptusage` WHERE ID=%s', (user_id,))
        data = cursor.fetchone()
        logger.info('got data. Writing it to data')


        if data is None:
            logger.info('Empty data')
            cursor.execute('INSERT INTO `gptusage` (ID, `uses`) VALUES (%s, %s)', (user_id, 0))
            connection.commit()
            logger.info(f'Новый пользователь с ID {user_id} создан.')
            cursor.execute('SELECT `uses` FROM `gptusage` WHERE ID=%s', (user_id,))
            data = cursor.fetchone()
            logger.info('got data. Writing it to data')

        usage = data['uses']
        

        if usage >= 100:
            connection.commit()
            connection.close()
            return False
        else:
            usage = usage + 1
            cursor.execute('UPDATE `gptusage` SET `uses` = %s WHERE id=%s;', (usage, user_id))
        connection.commit()

    connection.close()
    return True

print(func(4))