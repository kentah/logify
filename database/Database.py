import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import pool
import logging

from config import db
from database.setupSchema import tables


# logging setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('./logging/database.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Database:
    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1, 20, **kwargs)

    def temp_conn(self):
        """ Temporary connection for database and table creation """
        self.conn = psycopg2.connect('user={} password={}'.format(db['user'], db['password']))
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.conn.cursor()
        self.dbName = db['database']
        self.cursor.execute('SELECT 1 FROM pg_catalog.pg_database WHERE datname=\'{}\''.format(self.dbName))

    def create_database(self):
        """Create the postgresql database"""
        logger.debug(self.temp_conn())
        exists = self.cursor.fetchone()
        if not exists:
            self.cursor.execute('CREATE DATABASE {};'.format(self.dbName))
            print('Succesfully created database: {}'.format(self.dbName))
        else:
            print(f'Database {self.dbName} already exists')
        self.conn.close()
        self.cursor.close()

    def destroy_database(self):
        """Drop the postgresql database"""
        self.temp_conn()
        self.exists = self.cursor.fetchone()
        if self.exists:
            self.cursor.execute('DROP DATABASE {};'.format(self.dbName))
            print('Succesfully destroyed database: {}'.format(self.dbName))
        else:
            print(f'No such database, {self.dbName} exists')
        self.conn.close()
        self.cursor.close()


    def create_tables(self):
        """create tables without data for the postgresql database"""
        try:
            self.conn = psycopg2.connect('dbname={}'.format(db['database']))
            #self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor = self.conn.cursor()
            print('succesfully connected to db')
            for t in tables:
                print(t)
                logger.debug(self.cursor.execute(t))
                logger.debug(self.conn.commit())
            self.conn.close()
            self.cursor.close()
        except(Exception, psycopg2.DatabaseError) as err:
            logger.exception(err)
            self.conn.close()
            self.cursor.close()
        finally:
            if self.conn is not None:
                self.conn.close()

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()
    
    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


class CursorFromConnectionFromPool:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)



print(db['user'])
