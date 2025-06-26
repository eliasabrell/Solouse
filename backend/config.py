import os

class Config:
    PORT_SERVER = os.environ.get("PORT_SERVER") or 5000
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'sua-chave-secreta-muito-segura'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or 'sua-chave-jwt-segura'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/prod.db'
    DEBUG = False