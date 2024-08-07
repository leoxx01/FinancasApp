import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import EntriesModel

class Entrie():
    
    def __init__(self,params) -> None:
        
       self.params = params
    
    def createEntries(self) -> None:
        
        created_Entrie = EntriesModel.Entries(self.params).createEntriesBD()
        if(created_Entrie):
            return 'OK'
        
    def readEntries(self):
        read_Entrie = EntriesModel.Entries(self.params).readEntriesBD()

        for resultados in read_Entrie:
            print(resultados)

        if (read_Entrie):
            print("Leitura de entrada concedida !!")

    def updateEntries(self) -> None:
        update_Entrie = EntriesModel.Entries(self.params).updateEntriesBD()
        if(update_Entrie):
            print("Entrada Alterada!!")    

    def deleteEntries(self) -> None:
        delete_Entrie = EntriesModel.Entries(self.params).deleteEntriesBD()
        if(delete_Entrie):
            print("Entrada Deletada!!")

params = {
     "nome_entrada": "Salario",
     "valor": "1000",
     "id_user": "2",
     "id_entries":"2"
}

# Entrie(params).createEntries()
# Entrie(params).readEntries()
# Entrie(params).updateEntries()
# Entrie(params).deleteEntries()
