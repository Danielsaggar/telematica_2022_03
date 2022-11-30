import os
class Config:
    SECRET_KEY = os.urandom(24)

class Developmentconfig(Config):
    DEBUG = True
    MYSQL_HOST='sql10.freemysqlhosting.net'
    MYSQL_USER='sql10581986'
    MYSQL_PASSWORD='2E77cGtYtS'
    MYSQL_DB='sql10581986'

config ={
    'development': Developmentconfig
    
}