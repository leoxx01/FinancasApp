import sqlite3
import time

class Entries:

    def __init__(self, params) -> None:
        self.conn = sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()
        self.nome_entrada = str(params['nome_entrada'])
        self.valor = float(params['valor'])  
        self.id_user = int(params['id_user'])

 
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
                    return "Error"
            except sqlite3.Error as err:
                print(f"An error occurred while inserting data: {err}")
                self.conn.rollback()
                return "Error"
            finally:
                self.conn.close()
        self.conn.close()
        





