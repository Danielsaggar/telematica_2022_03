class ModelTable():
    @classmethod
    def positionA(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_a ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def positionB(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_b ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def positionC(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_c ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def positionD(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_d ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def positionE(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_e ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def positionF(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_f ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def positionG(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_g ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def positionH(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_h ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def prox(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id_Local,id_Visitante FROM partidos WHERE id_Estado=0"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def result(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id_Local,id_Visitante,GolesL,GolesV FROM partidos WHERE id_Estado=1"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)    
        