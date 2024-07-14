
import sqlite3

class Entries:

    def __init__(self,params) -> None:
        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = sqlite3.connect('my_database.db').cursor()
        self.nome_entrada = str(params['nome_entrada'])
        self.valor = params['valor']
        self.id_user = params['id_user']


    def createEntriesDB(self) -> str:
        try:
            
            sql = f"INSERT INTO entries (nameEntries,value,id_user) VALUES (?, ?, ?)"
            self.cursor.execute(sql,(self.nome_entrada,self.valor,self.id_user))
            self.conn.commit()
            

        except err:
            print(err)
            self.conn.rollback()    
        finally:
            self.conn.close()
        