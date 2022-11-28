from .entities.User import Users

def Cont(db,Grupo):
        try:                      
            cursor=db.connection.cursor()
            cursor.execute("SELECT count(Equipo) FROM grupo_"+Grupo)
            db.connection.commit()
            rows = cursor.fetchone()               
            return (rows) 
        except Exception as ex:
            raise Exception(ex)
        

class ModelGroups():
    @classmethod
    def create(self,db,Equipo,Grupo):
        try:               
            cursor=db.connection.cursor()
            if(Cont(db,Grupo)[0]<4):
                cursor.execute("INSERT INTO grupo_"+Grupo+" (Equipo,PJ) VALUES(%s,%s)",
                    (Equipo,0))
                db.connection.commit()
                print("Funciona") 
            else:
                cursor.execute("INSERT INTO grupo_r (Equipo,Grupo) VALUES(%s,%s)",
                    (Equipo,Grupo))
                db.connection.commit()
                print("Funciona") 
        except Exception as ex:
            raise Exception(ex)
        
    