class ModelGame():
    @classmethod
    def Online(self,db):
        try:
            cursor=db.connection.cursor()
            sql="select id_Partido from partidos WHERE id_Estado=1"
            cursor.execute(sql)
            rows = cursor.fetchone()    
            print(rows[0])
            return (rows[0])            
        except Exception as ex:
            raise Exception(ex)