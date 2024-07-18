
import sqlite3

class Investments:

    def __init__(self,params) -> None:
        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()

        
        self.name_Investiments = params['name_Investiments']
        self.type_investments = params['type_investments']
        self.value = params['value']
        self.profitability = params['profitability']
        self.id_user = params['id_user']
        self.id_investimentos = params['id_investimentos']


    def createInvestmentsDB(self) -> str:
        retries = 5
        while retries > 0:
            try:
                
                sql = f"INSERT INTO investments (name_Investiments,type_investments,value,profitability,id_user) VALUES (?, ?, ?, ?, ?)"
                self.cursor.execute(sql,(self.name_Investiments,self.type_investments,self.value,self.profitability,self.id_user))
                self.conn.commit()
                return "OK"
                
            except sqlite3.OperationalError as err:
                if 'database is locked' in str(err):
                    print("Database is locked, retrying...")
                    retries -= 1
                    time.sleep(1)  
                else:
                    print(f"An operational error occurred: {err}")
                    self.conn.rollback()
                    
            except sqlite3.Error as err:
                print(f"An error occurred while inserting data: {err}")
                self.conn.rollback()
                
            finally:
                
                self.conn.close()

    def updateInvestmentsDB(self) ->str:
        retries = 5
        while retries > 0:
            try:
                sql = f" UPDATE investments SET name_Investiments = ? , type_investments = ? , value = ? ,profitability = ? WHERE id = ?"
                self.cursor.execute(sql,(self.name_Investiments,self.type_investments,self.value,self.profitability,self.id_investimentos ))
                self.conn.commit()
                return "OK"
            except sqlite3.OperationalError as err:
                if 'database is locked' in str(err):
                    print("Database is locked, retrying...")
                    retries -= 1
                    time.sleep(1)  
                else:
                    print(f"An operational error occurred: {err}")
                    self.conn.rollback()
                    return "Error" 
            except sqlite3.Error as err:
                print(f"An error occurred while inserting data: {err}")
                self.conn.rollback()
                return "Error"
            finally:
                self.conn.close()

    def deleteInvestmentsBD(self) -> str :
        retries = 5
        while retries >0:
            try:
                sql = f" DELETE FROM investments WHERE id = ?"
                self.cursor.execute(sql,(self.id_investimentos))
                self.conn.commit()
                return "OK"
            except sqlite3.OperationalError as err:
                if 'database is locked' in str(err):
                    print("Database is locked, retrying...")
                    retries -= 1
                    time.sleep(1)  
                else:
                    print(f"An operational error occurred: {err}")
                    self.conn.rollback()
                    return "Error" 
            except sqlite3.Error as err:
                print(f"An error occurred while inserting data: {err}")
                self.conn.rollback()
                return "Error"
            finally:
                self.conn.close()
            

    