def lastdata(db,id_Partido):
    try:
        id_Partido=str(id_Partido)
        cursor=db.connection.cursor()        
        cursor.execute("select AmarillaL,AmarillaV,RojaL,RojaV,GolesL,GolesV,EsquinaL,EsquinaV,ArcoL,ArcoV,OffsideL,OffsideV from partidos WHERE id_Partido = "+id_Partido+"")
        rows = cursor.fetchone()    
        return (rows)            
    except Exception as ex:
        raise Exception(ex)


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
    
    @classmethod
    def update(self,db,id_Partido, AmarillaL, AmarillaV, RojaL, RojaV,GolesL, GolesV, 
    EsquinaL, EsquinaV, ArcoL, ArcoV, OffsideL, OffsideV):
        try:
            cursor=db.connection.cursor()    
            data=lastdata(db,id_Partido) 
            cursor.execute("UPDATE partidos SET AmarillaL= %s, AmarillaV= %s, RojaL= %s, RojaV= %s,GolesL= %s,GolesV= %s,EsquinaL= %s,EsquinaV= %s,ArcoL= %s,ArcoV= %s,OffsideL= %s,OffsideV= %s WHERE id_Partido = %s",
            (AmarillaL+data[0], AmarillaV+data[1], RojaL+data[2], RojaV+data[3], GolesL+data[4], GolesV+data[5], EsquinaL+data[6], EsquinaV+data[7], ArcoL+data[8], ArcoV+data[9], OffsideL+data[10], OffsideV+data[11], id_Partido))                   
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)