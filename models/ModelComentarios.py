from .entities.User import Users


class ModelComentarios():
    @classmethod
    def last(self,db):
        try:
            cursor=db.connection.cursor()
            sql="select * from comentarios ORDER BY idComentarios DESC"
            cursor.execute(sql)
            rows = cursor.fetchone()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def clean(self,db):
        try:
            cursor=db.connection.cursor()
            sql="DELETE FROM comentarios"
            cursor.execute(sql)    
            db.connection.commit()
            print("Funciona")        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def new(self,db,num,comment):
        try:
            cursor=db.connection.cursor()
            cursor.execute("INSERT INTO comentarios (idComentarios, Comentario) VALUES(%s,%s)",
                (num,comment))
            db.connection.commit()
            print("Funciona")     
        except Exception as ex:
            raise Exception(ex)