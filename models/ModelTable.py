from .entities.User import Users


class ModelTable():
    @classmethod
    def positions(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM Posiciones ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)