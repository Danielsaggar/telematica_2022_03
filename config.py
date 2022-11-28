import os
class Config:
    SECRET_KEY = os.urandom(24)

class Developmentconfig(Config):
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='qatar'

config ={
    'development': Developmentconfig
    
}