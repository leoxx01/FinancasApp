import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import EntriesModel



class Entrie():
    
    def __init__(self,params) -> None:
        
       self.params = params
    
    def createEntries(self) -> None:

        createdEntrie = EntriesModel.Entries(self.params).createEntriesDB()
        if(createdEntrie):
            print('Entrada Criado!!!')
        
        



params = {
    "nome_entrada": "salario",
    "valor": "100",
    "id_user": "1"
}

Entrie(params).createEntries()
