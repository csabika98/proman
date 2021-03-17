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
def register_user(cursor:RealDictCursor,password:str, email:str, created_on:str) -> list:
    cursor.execute("""INSERT INTO accounts (password, email, created_on) VALUES (%s,%s,%s)""",(password, email, created_on))