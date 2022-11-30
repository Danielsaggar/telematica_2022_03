class Modelprogramacion():
    @classmethod
    def Group(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT Grupo FROM equipos group by Grupo"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def Arbitro(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM arbitros"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)        
    @classmethod
    def Visitantes(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT Equipo FROM equipos"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)  

    @classmethod                     
    def Locales(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT Equipo FROM equipos"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)               
    @classmethod                     
    def Estadios(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id_estadio,Estadio FROM estadios"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)   
    @classmethod                     
    def Create(self,db,id_Local, id_Visitante, id_Estadio, id_Arbitro,Hora,Fecha):
        try:
            Hora=str(Hora)
            Fecha=str(Fecha)
            cursor=db.connection.cursor()
            cursor.execute("INSERT INTO partidos (id_Local, id_Visitante, id_Estadio, id_Arbitro,Hora,Fecha) VALUES(%s,%s,%s,%s,%s,%s)",
                (id_Local, id_Visitante, id_Estadio, id_Arbitro,Hora,Fecha))
            db.connection.commit()
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)  