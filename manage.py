import psycopg2
import os
from app.api.v2.auth.auth import User

class ConnectDB:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                os.getenv('DATABASE_URL')
                )
            self.cursor = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

class CreateTables(ConnectDB):

    def __init__(self):
        super().__init__()

    def create_tables(self):

        queries = [
        """
        CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            username VARCHAR NOT NULL UNIQUE,
            email VARCHAR NOT NULL UNIQUE,
            password VARCHAR NOT NULL,
            is_admin BOOL NOT NULL
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS meals(
            id serial PRIMARY KEY,
            name VARCHAR NOT NULL,
            description VARCHAR NOT NULL , 
            price INT NOT NULL
            
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS orders(
            id serial PRIMARY KEY,
            username VARCHAR NOT NULL,
            title VARCHAR NOT NULL,
            description VARCHAR NOT NULL,
            price INT NOT NULL,
            status VARCHAR NOT NULL,
            order_date TIMESTAMP
        )
        """
        ]

        for query in queries:
            self.cursor.execute(query)

        self.conn.commit()
        self.cursor.close()

    def drop(self):
        queries = [
            '''
            DROP TABLE IF EXISTS users
            ''',
            '''
            DROP TABLE IF EXISTS meals
            ''',
            '''
            DROP TABLE IF EXISTS orders
            '''
        ]

        for query in queries:
            self.cursor.execute(query)

        self.conn.commit()
        self.cursor.close()

    def add_admin(self):
        admin = User(username='Useradmin', email='admin@gmail.com',
                 password='Admin123', is_admin=True)
        admin.add()


if __name__ == '__main__':
    CreateTables().drop()
    CreateTables().create_tables()
    CreateTables().add_admin()
