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

        pass

        #Criação das tabelas caso não existam
        CreateTables.CreateAllTabels().createTables()


Connect()

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
teste = cursor.execute("SELECT * FROM typeEntries  ").fetchall()
# teste = cursor.execute("SELECT * FROM Entries WHERE id_user = '17' ").fetchall()
# teste = cursor.execute('INSERT INTO typeEntries (type_name) VALUES ("Salario")')
conn.commit()
rows = teste
print(teste)
for row in rows:
    print(row)


# cursor.execute("DROP TABLE users").fetchall()


