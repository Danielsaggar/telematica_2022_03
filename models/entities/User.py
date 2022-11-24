from werkzeug.security import check_password_hash, generate_password_hash

class Users():

    def __init__(self, id, user, password, type) -> None:
        self.id=id
        self.user=user
        self.password=password
        self.type=type

    
    @classmethod
    def check(self, hashed_password, password):
        return check_password_hash(hashed_password,password)
    
    @classmethod
    def encrypt(self, password):        
        return generate_password_hash(password)

    
