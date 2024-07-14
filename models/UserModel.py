import sys
import os
import sqlite3

class Users:

    def __init__(self,params) -> None:
        self.conn =  sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()
        self.nome = str(params['nome'])
        self.email = params['email']
        self.senha = params['senha']

    def createUserDB(self) -> str:
        try:
            strValues = ""
            sql = f"INSERT INTO users (name,email,password) VALUES (?, ?, ?)"
            self.cursor.execute(sql,(self.nome,self.email,self.senha))
            self.conn.commit()
        except(err):
            print(err)
            self.conn.rollback()    
        finally:
            self.conn.close()


