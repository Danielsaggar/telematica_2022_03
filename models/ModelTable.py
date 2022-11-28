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
            sql="SELECT * FROM grupo_F ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def positionG(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_G ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def positionH(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM grupo_H ORDER BY Pts desc"
            cursor.execute(sql)
            rows = cursor.fetchall()    
            return (rows)            
        except Exception as ex:
            raise Exception(ex)
        