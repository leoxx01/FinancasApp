
import sqlite3

class Investments:

    def __init__(self,params) -> None:
        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = sqlite3.connect('my_database.db').cursor()

        
        self.name_Investiments = params['name_Investiments'],
        self.type_investments = params['type_investments'],
        self.value = params['value'],
        self.profitability = params['profitability'],
        self.id_user = params['id_user']


    def createInvestmentsDB(self) -> str:
        try:
            
            sql = f"INSERT INTO leaves (name_Investiments,type_investments,value,profitability,id_user) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(sql,(self.name_Investiments,self.type_investments,self.value,self.profitability,self.id_user))
            self.conn.commit()
            return "OK"
            

        except err:
            print(err)
            self.conn.rollback()    
        finally:
            self.conn.close()
        

    