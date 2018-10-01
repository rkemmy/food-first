import psycopg2
import os

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
            price INTEGER NOT NULL,
            description VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS orders(
            id serial PRIMARY KEY,
            username VARCHAR NOT NULL,
            status VARCHAR NOT NULL,
            order_date TIMESTAMP
        )
        """
        ]

        for query in queries:
            self.cursor.execute(query)

        self.conn.commit()
        self.cursor.close()


if __name__ == '__main__':
    CreateTables().create_tables()
