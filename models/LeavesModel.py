
import sqlite3
import time

class Leaves:

    def __init__(self,params) -> None:
        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()

        self.nameLeave = str(params['nameLeave'])
        self.value = str(params['value'])
        self.installments = str(params['installments'])
        self.pays_installments = str(params['pays_installments'])
        self.pays_finish = str(params['pays_finish'])
        self.id_user = str(params['id_user'])


    def createLeavesDB(self) -> str:
        retries = 5
        while retries > 0:
            try:    
                sql = f"INSERT INTO leaves (nameLeave,value,installments,pays_installments,pays_finish,id_user) VALUES (?, ?, ?, ?, ?, ?)"
                self.cursor.execute(sql , (self.nameLeave, self.value, self.installments, self.pays_installments, self.pays_finish, self.id_user))
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
            

    