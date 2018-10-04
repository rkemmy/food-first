![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Build Status](https://travis-ci.org/rkemmy/food-first.svg?branch=ft-delete-order-%23160605330)](https://travis-ci.org/rkemmy/food-first)
[![Coverage Status](https://coveralls.io/repos/github/rkemmy/food-first/badge.svg?branch=ft-delete-order-%23160605330)](https://coveralls.io/github/rkemmy/food-first?branch=ft-delete-order-%23160605330)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)


# Food-First

Food-First is an application that allows users to order mouth watering delicacies with a single tap.

### Prerequisites

What you need to get started:

- [Python 3](https://www.python.org/download/releases/3.0/)

- [virtualenv](https://virtualenv.pypa.io/en/stable/)

- [Pip](https://pip.pypa.io/en/stable/installing/)

- [PostgreSQL](https://www.postgresql.org/download/)

- [Flask](http://flask.pocoo.org/)

#### Technologies used
    - Python 3.7
    - Flask
    - Flask_RESTful
    - Travis CI
    - Flask-JWT-Extended
    - Psycopg2

### Installing

- #### *Make sure PostgreSQL server is installed and running, then create databases:*

    - Log in to postgres account 

        ``` 
        $ psql --user postgres 
        ```

    - Create main database 

        ``` 
        postgres=# CREATE DATABASE fastfood; 
        ```

    - Create test database 
    
        ``` 
        postgres=# create database fastfoodtest_db; 
        ```

- #### *Clone this repo :*

    ```
    $ git clone https://github.com/rkemmy/food-first.git
    ```

- ####  *Move to project directory :*
    
    ``` 
    $ cd food-first 
    ```

- #### *Create your Virtual Environment :*
    
    ```
    $ python3.7 -m venv [environment-name]
    ```

- #### *Activate your virtual environment :*
    
    ```
    $ source [environment-name]/bin/activate 
    ```

- #### *Install project requirements :*
    
    ```
    $ pip install -r requirements.txt 
    ```

- #### *Set up database :*
    
    ```
    $ python3 manage.py  
    
    ``` 

- #### *Start the app :*
    
    ```
    $ flask run 
    ``` 

- *You can now access the API from:* 
    
    ```
    http://localhost:5000/api/v2
    ``` 


## Running the tests

- With Coverage Report: 
    
    ```
    $ nosetests --with-coverage --cover-package=app/api/v2 --cover-html 
    ```

## Documentation

Documentation can be accessed on:

    http://localhost:5000/apidocs

## Endpoints

| URL                                                       | Methods | Description              | Requires Auth  |
|-----------------------------------------------------------|---------|--------------------------|----------------|
| `/api/v2`                                                 | GET     | The base URL             | FALSE          |
| `/api/v2/auth/signup`                                     | POST    | Register User            | FALSE          |
| `/api/v2/auth/login`                                      | POST    | Login User               | FALSE          |
| `/api/v2/menu`                                            | POST    | Creates Meal             | TRUE           |
| `/api/v2/menu`                                            | GET     | Gets all meals           | FALSE          |
| `/api/v2/users/orders`                                    | POST    | Creates an order         | TRUE           |
| `/api/v2/users/orders`                                    | GET     | Returns all users orders | TRUE           |
| `/api/v2/users/orders/<int:id>`                           | GET     | Returns one order        | TRUE           |
| `/api/v2/users/history`                                   | GET     | Gets user's order history| TRUE           |
| `/api/v2/users/orders/<int:id>`                           | PUT     | Updates order status     | TRUE           |
| `/api/v2/users/orders/<int:id>`                           | DELETE  | Deletes an order         | TRUE           |
| `/api/v2/menu/<int:id>`                                   | DELETE  | Deletes a meal item      | TRUE           |


## Built With

- [Flask](http://flask.pocoo.org/)

Copyright (c)2018 **Risper Kemunto**
