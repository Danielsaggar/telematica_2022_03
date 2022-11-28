class ModelPlayer():
    @classmethod
    def Nation(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT Equipo FROM equipos"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def create(self,db,Nombre, Apellido, Equipo, Numero):
        try:
            cursor=db.connection.cursor()                        
            cursor.execute("INSERT INTO jugadores (Nombre, Apellido, Equipo, Numero) VALUES(%s,%s,%s,%s)",
                (Nombre, Apellido, Equipo, Numero))
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def AllPlayer(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM jugadores"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)