from .entities.User import Users


class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT idUser, User, Password, Type FROM user
                    WHERE User= '{}'""".format(user.user)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=Users(row[0], row[1], Users.check(row[2],user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self,db,user):        
        try:
            cursor=db.connection.cursor()
            sql="""SELECT User, Type, Cell FROM user
                    WHERE idUser= '{}'""".format(user)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:                
                logged_user=Users(row[2], row[0], None, row[1])
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod      
    def create(self,db,user):
        try:
            cursor=db.connection.cursor()                        
            cursor.execute("INSERT INTO user (User, Password, Type, Cell) VALUES(%s,%s,%s,%s)",
                (user.user, Users.encrypt(user.password),"1",user.id))
            db.connection.commit()
            print("Funciona")
        except Exception as ex:
            raise Exception(ex)