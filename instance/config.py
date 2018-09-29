import os

class Config(object):
    """ Parent configuration class """
    pass
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """ Development configuration class that inherits from the Config Parent Class"""
    DEBUG = True
    
class TestConfig(Config):
    """ Testing configuration class that inherits from the Config Parent Class"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')

class ProductionConfig(Config):
    """ Prduction configuration class that inherits from the Config Parent Class"""
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestConfig,
    'production' : ProductionConfig
}
