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

class MealItem(ConnectDB):
    def __init__(self, name=None, description=None, price=None):
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def add(self):
        ''' Add meal item to meals table'''
        self.cursor.execute(
            ''' INSERT INTO meals(name, description, price) VALUES(%s, %s, %s)''',
            (self.name, self.description, self.price))

        self.connection.commit()
        self.cursor.close()

    def get_meal_by_name(self, name):
        '''fetch an item by id'''
        self.cursor.execute(""" SELECT * FROM meals WHERE name = '%s' """ %
                            (name))

        meal = self.cursor.fetchone()

        self.connection.commit()
        self.cursor.close()

        if meal:
            return self.objectify(meal)
        return None

    def get_all_meals(self):
        '''  Get all meal items '''
        self.cursor.execute(''' SELECT * FROM meals''')

        meals = self.cursor.fetchall()

        self.connection.commit()
        self.cursor.close()

        if meals:
            return [self.objectify(meal) for meal in meals]
        return None

    def serialize(self):
        ''' Return object as dictionary '''
        return dict (
            id = self.id,
            name = self.name,
            description = self.description,
            price = self.price
        )

    def objectify(self, data):
        ''' map tuple to an object '''
        item = MealItem(name=data[1], description=data[2], price=data[3])
        item.id = data[0]
        self = item
        return self
        
class Order(ConnectDB):
    def __init__(self,
                # id = None,
                 username=None,
                 title=None,
                 description = None,
                 price=None,
                 status="Pending"):
        super().__init__()
        self.username = username
        self.title = title
        self.description = description
        self.price = price
        self.status = status
        

    def add(self):
        ''' Add food order to database'''
        print(self.username)
        self.cursor.execute(
            """ INSERT INTO orders(username, title, description, price, status) VALUES('%s','%s','%s','%s','%s')""" %
            (self.username, self.title, self.description, self.price,self.status))

        self.connection.commit()
        self.cursor.close()

    def get_by_id(self, order_id):
        '''fetch an order by id'''
        self.cursor.execute(''' SELECT * FROM orders WHERE id=%s''',
                            (order_id, ))

        order = self.cursor.fetchone()

        self.connection.commit()
        self.cursor.close()

        if order:
            return self.objectify(order)
        return None

    def serialize(self):
        ''' return object as a dictionary '''
        return dict (
            id = self.id,
            title = self.title,
            description = self.description,
            price = self.price,
            status = self.status,
            date = self.date
        )
    
    def objectify(self, data):
        ''' map tuple to an object '''
        order = Order(
            username=data[1],
            description=data[2],
            title=data[3],
            price=data[4],
            status=data[5])
        order.id = data[0]
        order.date = str(data[6])
        self = order
        return self
