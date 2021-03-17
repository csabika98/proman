import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictConnection, RealDictCursor 
import connection_string

@connection_string.connection_handler
def select_accounts(cursor: RealDictCursor,) -> list:
    query = f"""
        SELECT *
        FROM accounts;
    """
    cursor.execute(query)
    return cursor.fetchall()


