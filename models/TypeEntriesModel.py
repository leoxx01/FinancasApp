import sqlite3
import time

class TypeEntries:
    
    def __init__(self,params) -> None:

        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()
        self.nameEntrie = params['nameEntrie']

    def createTypeEntrie(self)-> str:
            retries = 5
            while retries >0:
                try:
                    sql = f'INSERT INTO typeEntries (type_name) VALUES ("{self.nameEntrie}")' 
                    querryExecute = self.cursor.execute(sql)
                    self.conn.commit()

                    if querryExecute:
                        self.conn.commit()
                        return "OK"
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