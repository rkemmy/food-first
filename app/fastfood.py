user_table = """
CREATE TABLE IF NOT EXIST users(
    user_id serial PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    email VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    type BOOLEAN DEFAULT 'user'
)
"""

meals_table = """
CREATE TABLE IF NOT EXIST meals(
    meal_id serial PRIMARY KEY,
    price numeric NOT NULL,
    description VARCHAR(20) NOT NULL,
    name VARCHAR(20) NOT NULL,  
)
"""

category_table = """
CREATE TABLE IF NOT EXIST category(
    category_id serial PRIMARY KEY,
    category_name VARCHAR NOT NULL,
)
"""

order_table = """
CREATE TABLE IF NOT EXIST orders(
    meal_id NOT NULL, 
    user_id NOT NULL,
    qty INT NOT NULL,
    status VARCHAR(10) NOT NULL,
    order_date INT64 TIMESTAMP,
    delivery_date INT64 TIMESTAMP,
)
"""
tables = [user_table, meals_table, category_table, order_table ]