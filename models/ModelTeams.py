from .entities.User import Users

def convertbinary(filename):
    with open(filename,'rb') as file:
        binarydata=file.read()
    return binarydata

def convertfile(binarydata,filename):
    with open(filename,'wb') as file:
        file.write(binarydata)    


class ModelTeams():
    @classmethod
    def create(self,db,Id_Grupo, Equipo, Escudo, Grupo, Entrenador):
        try:
            Binpic=convertbinary(Escudo)
            cursor=db.connection.cursor()
            cursor.execute("INSERT INTO equipos (Id_Grupo, Equipo, Escudo, Grupo, Entrenador) VALUES(%s,%s,%s,%s,%s)",
                (Id_Grupo, Equipo, Binpic, Grupo, Entrenador))
            db.connection.commit()
            print("Funciona")     
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self,db,id):
        try:
            id=str(id)
            cursor=db.connection.cursor()                        
            cursor.execute("DELETE FROM equipos WHERE Equipo = '"+id+"'")
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def edit(self,db,id,Equipo, Escudo, Id_Grupo, Grupo, Entrenador):
        try:
            id=str(id)  
            Binpic=convertbinary(Escudo)          
            cursor=db.connection.cursor()                 
            cursor.execute("UPDATE equipos SET Equipo=%s, Escudo=%s, Id_Grupo=%s, Grupo=%s, Entrenador=%s WHERE Equipo = '"+id+"'",
            (Equipo, Binpic, Id_Grupo, Grupo, Entrenador))
            db.connection.commit()
            print("Funciona")    
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def escudo(self,db,Id_Grupo, Equipo, Escudo, Grupo, Entrenador):
        try:
            Binpic=convertbinary(Escudo)
            cursor=db.connection.cursor()
            cursor.execute("INSERT INTO equipos (Id_Grupo, Equipo, Escudo, Grupo, Entrenador) VALUES(%s,%s,%s,%s,%s)",
                (Id_Grupo, Equipo, Binpic, Grupo, Entrenador))
            db.connection.commit()
            print("Funciona")     
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def AllTeams(self,db):
        try:
            cursor=db.connection.cursor()
            sql="SELECT * FROM equipos"
            cursor.execute(sql)
            rows = cursor.fetchall()  
            ruta='static/resources/escudos/'
            lista=()    
            i=0          
            for p in rows:
                ruta='static/resources/escudos/'
                ruta=ruta+p[0]+'.jpg'
                convertfile(p[1],ruta)                                
                lst=list(lista)
                rut = "../../"+ruta   
                lst.append(rut)  
                lista=tuple(lst)            
            print(lista)
            return (rows, lista)            
        except Exception as ex:
            raise Exception(ex)