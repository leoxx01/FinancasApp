import sqlite3
import sys
import os
#Append dir que contem SQL
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'venv\sql'))
sys.path.append(module_path)

# Arquivo que cria tabela caso não exista tabela 
import CreateTables

class Connect:
    def __init__(self) -> None:
<<<<<<< HEAD
        pass
=======
        #Criação das tabelas caso não existam
        CreateTables.CreateAllTabels().createTables()


Connect()

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
teste = cursor.execute("SELECT * FROM investments").fetchall()
rows = teste
print(teste)
for row in rows:
    print(row)


# cursor.execute("DROP TABLE users").fetchall()

>>>>>>> 1c5695c13c084705dc38ffd4ced4e1ceee203783
