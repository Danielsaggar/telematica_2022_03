class ModelGame():
    @classmethod
    def Online(self,db):
        try:
            cursor=db.connection.cursor()
            sql="select id_Partido from partidos WHERE Online=1"
            cursor.execute(sql)
            rows = cursor.fetchone()    
            print(rows[0])
            return (rows[0])            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def Score(self,db):
        try:
            cursor=db.connection.cursor()
            sql="select AmarillaL, AmarillaV, RojaL, RojaV, GolesL, GolesV, EsquinaL, EsquinaV, ArcoL, ArcoV, OffsideL, OffsideV from partidos WHERE Online=1"
            cursor.execute(sql)
            rows = cursor.fetchone()                
            return (rows)            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def Teams(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT Equipo, Grupo FROM equipos"
            cursor.execute(sql)
            rows = cursor.fetchall()              
            return (rows)            
        except Exception as ex:
            raise Exception(ex)