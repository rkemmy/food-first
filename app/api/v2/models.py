import os
import psycopg2
from datetime import datetime
from werkzeug.security import generate_password_hash

class ConnectDB:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                os.getenv('DATABASE_URL')
                )
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

class User(ConnectDB):
    def __init__(self,
                 username=None,
                 email=None,
                 password=None,
                 is_admin=False):
        super().__init__()
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def add(self):
        ''' Add uset to user table'''
        self.cursor.execute(
            ''' INSERT INTO users(username, email, password, is_admin) VALUES(%s, %s,%s, %s)''',
            (self.username, self.email, self.password, self.is_admin))

        self.connection.commit()
        self.cursor.close()

    def get_user_by_username(self, username):
        ''' get user by username '''
        self.cursor.execute(''' SELECT * FROM users WHERE username=%s''',
                            (username, ))

        user = self.cursor.fetchone()

        self.connection.commit()
        self.cursor.close()

        if user:
            return self.objectify_user(user)
        return None

    def get_user_by_email(self, email):
        ''' get user by email '''
        self.cursor.execute(''' SELECT * FROM users WHERE email=%s''',
                            (email, ))

        user = self.cursor.fetchone()

        self.connection.commit()
        self.cursor.close()

        if user:
            return self.objectify_user(user)
        return None

    def serialize(self):
        '''return an object as dictionary'''
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
            is_admin=self.is_admin
            )

    def objectify_user(self, data):
        ''' change a tuple user to an object '''
        self.id = data[0]
        self.username = data[1]
        self.email = data[2]
        self.password = data[3]
        self.is_admin = data[4]

        return self            