from .entities.User import Users

class ModelArbitrator():
    @classmethod
    def AllArbitrator(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id_arbitro,Nombre,Equipo as Procedencia FROM Arbitros, Equipos WHERE Procedencia=id_Equipos"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def create(self,db,name,country):
        try:
            cursor=db.connection.cursor()                        
            cursor.execute("INSERT INTO Arbitros (Nombre,Procedencia) VALUES(%s,%s)",
                (name,country))
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)