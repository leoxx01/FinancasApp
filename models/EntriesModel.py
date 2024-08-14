import sqlite3
import time

class Entries:

    def __init__(self, params) -> None:
        self.conn = sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()

        self.params = params

        self.nome_entrada = str(params['nome_entrada'])
        self.valor = str(params['valor'])  
        self.id_user = str(params['id_user'])
        
    def createEntriesDB(self) -> str:
        retries = 5
        while retries > 0:
            try:
                sql = "INSERT INTO entries (nameEntries, value, id_user) VALUES (?, ?, ?)"
                self.cursor.execute(sql, (self.nome_entrada, self.valor, self.id_user))
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

    def updateEntriesBD(self) ->str:
        retries = 5
        while retries > 0:
            try:
                sql = f" UPDATE entries SET nameEntries = ?, value = ? WHERE id = ?"
                self.cursor.execute(sql,(self.nome_entrada, self.valor, self.params['id']))
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

    def deleteEntriesBD(self) -> str :
        idEntrada = self.params['id']
        retries = 5
        while retries >0:
            try:
                sql = f" DELETE FROM entries WHERE id = {idEntrada}"
                
                self.cursor.execute(sql)
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
        
    def getItemById(self,dataInicio,dataFim)-> str:
        retries = 5
        while retries >0:
            try:
                sql = f" SELECT * FROM entries WHERE id_user = '{str(self.id_user)}' " 
                querryExecute = self.cursor.execute(sql)
                self.conn.commit()

                if querryExecute:
                    self.conn.commit()
                    return querryExecute.fetchall() 
                else:
                    return "NOK"
                
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
    def getItemsOnDate(self)->str:
        retries = 5
        while retries >0:
            try:
                sql = f" SELECT * FROM entries WHERE id_user = '{str(self.id_user)}' and date_created >= '{str(self.params['dataIncio'])}' and date_created <= '{str(self.params['dataFim'])}' and nameEntries = '{self.nome_entrada}'" 
                querryExecute = self.cursor.execute(sql)
                self.conn.commit()

                if querryExecute:
                    self.conn.commit()
                    return querryExecute.fetchall() 
                else:
                    return "NOK"
                
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




