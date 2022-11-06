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