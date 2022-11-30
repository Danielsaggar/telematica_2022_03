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
            sql="SELECT Nombre FROM arbitros"
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
            sql="SELECT Estadio FROM estadios"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)        