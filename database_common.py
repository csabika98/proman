import os
import psycopg2
import psycopg2.extras

os.environ['PSQL_USER_NAME'] = 'kkwzuforeqybeg'
os.environ['PSQL_PASSWORD'] = '28e2b153d29f9d69d868f598b4d9be9a0315fb197d44ed503ea560a075024291' # change this to your password!
os.environ['PSQL_HOST'] = 'ec2-54-228-9-90.eu-west-1.compute.amazonaws.com'
os.environ['PSQL_DB_NAME'] = 'd7733afmvqrtnq'

def get_connection_string():
    # setup connection string
    # to do this, please define these environment variables first


    user_name = os.environ.get('PSQL_USER_NAME')
    password = os.environ.get('PSQL_PASSWORD')
    host = os.environ.get('PSQL_HOST')
    database_name = os.environ.get('PSQL_DB_NAME')

    env_variables_defined = user_name and password and host and database_name

    if env_variables_defined:
        # this string describes all info for psycopg2 to connect to the database
        return 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
    else:
        raise KeyError('Some necessary environment variable(s) are not defined')


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, kwargs):
        connection = open_database()
        # we set the cursor_factory parameter to return with a RealDictCursor cursor (cursor which provide dictionaries)
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper