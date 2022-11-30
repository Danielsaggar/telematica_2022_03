from .entities.User import Users

class ModelStadium():
    @classmethod
    def AllStadium(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id_estadio,Estadio,Capacidad,Ubicación FROM Estadios"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def create(self,db,name,country,capacidad):
        try:
            cursor=db.connection.cursor()                        
            cursor.execute("INSERT INTO Estadios (Estadio,Capacidad,Ubicación) VALUES(%s,%s,%s)",
                (name,capacidad,country))
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def edit(self,db,id,name,country,capacidad):
        try:
            cursor=db.connection.cursor()                
            cursor.execute("UPDATE Estadios SET Estadio=%s, Capacidad=%s, Ubicación=%s WHERE id_estadio = %s",
            (name,capacidad,country,id))  
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self,db,id):
        try:
            id=str(id)
            cursor=db.connection.cursor()                        
            cursor.execute("DELETE FROM Estadios WHERE id_estadio = "+id+"")
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)