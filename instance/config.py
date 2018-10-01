import os

class Config(object):
    """ Parent configuration class """
    pass
    CSRF_ENABLED = True
    
class DevelopmentConfig(Config):
    """ Development configuration class that inherits from the Config Parent Class"""
    DEBUG = True
    
class TestConfig(Config):
    """ Testing configuration class that inherits from the Config Parent Class"""
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    """ Prduction configuration class that inherits from the Config Parent Class"""
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestConfig,
    'production' : ProductionConfig
}