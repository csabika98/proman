from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_accounts(cursor: RealDictCursor) -> list:
    query = """
        SELECT *
        FROM accounts"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def register_new_user(cursor:RealDictCursor,password:str, email:str, created_on:str) -> list:
    cursor.execute("""INSERT INTO accounts (password, email, created_on) VALUES (%s,%s,%s)""",(password, email, created_on))

@database_common.connection_handler
def get_user_by_email_and_pass(cursor:RealDictCursor, email, password) -> list:
    query = f"""
            SELECT *
            FROM accounts
            WHERE email = '{email}' AND password = '{password}'
    """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_email(cursor:RealDictCursor, email:str) -> list:
    query = f"""
            SELECT email FROM accounts WHERE email='{email}'"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_password(cursor:RealDictCursor, password:str) -> list:
    query = f"""
            SELECT password FROM accounts WHERE password='{password}'"""
    cursor.execute(query)
    return cursor.fetchall()




