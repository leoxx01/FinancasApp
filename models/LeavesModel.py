
import sqlite3

class Leaves:

    def __init__(self,params) -> None:
        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = sqlite3.connect('my_database.db').cursor()

        self.nameLeave = params['nameLeave'],
        self.value = params['value'],
        self.installments = params['installments'],
        self.pays_installments = params['pays_installments'],
        self.pays_finish = params['pays_finish'],
        self.id_user = params['id_user']


    def createLeavesDB(self) -> str:
        try:
            
            sql = f"INSERT INTO leaves (nameLeave,value,installments,pays_installments,pays_finish,id_user) VALUES (?, ?, ?, ?, ?, ?)"
            self.cursor.execute(sql,(self.nameLeave,self.value,self.installments,self.pays_installments,self.pays_finish,self.id_user))
            self.conn.commit()
            return "OK"
            

        except err:
            print(err)
            self.conn.rollback()    
        finally:
            self.conn.close()
        

    