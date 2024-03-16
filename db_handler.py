import pymysql
from mysql.connector import Error
from functools import wraps

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
        print(usage)
        if usage > 10:
            raise ValueError(f'Пользователь с ID {user_id} превысил лимит использования.')
        else:
            usage = usage + 1
            print('should make', usage)
            cursor.execute('UPDATE `gptusage` SET `uses` = %s WHERE id=%s;', (usage, user_id))
        connection.commit()
        #     # Если usage больше 10, выдаем ошибку
        #     raise ValueError(f'Пользователь с ID {user_id} превысил лимит использования.')
        # else:
        #     logger.info(f'Пользователь с ID {user_id} имеет {usage} использований.')

    connection.close()

func(3)