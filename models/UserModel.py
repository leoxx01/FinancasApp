import time
import sqlite3

class Users:

    def __init__(self,params) -> None:
        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()
        
        self.nome = params['nome']
        self.email = params['email']
        self.senha = params['senha']
        self.id_user = params['id']

    def createUserDB(self) -> str:
        retries = 5
        while retries > 0:
            try:
                sql = f"INSERT INTO users (name,email,password) VALUES (?, ?, ?)"
                self.cursor.execute(sql,(self.nome,self.email,self.senha))
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

    def updateUserBD(self) ->str:
        retries = 5
        while retries >0:
            try:
                sql = f" UPDATE users SET name = ?, email = ?, password = ?  WHERE id = ?"
                self.cursor.execute(sql,(self.nome,self.email,self.senha,self.id_user))
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
    def deleteUserBD(self) -> str :
        retries = 5
        while retries >0:
            try:
                sql = f" DELETE FROM users WHERE id = ?"
                self.cursor.execute(sql,(self.id_user))
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