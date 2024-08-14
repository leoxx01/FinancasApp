import sys
import os
from datetime import datetime

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import EntriesModel

class Entrie():
    
    def __init__(self,params) -> None:
        
        self.params = params

        data = datetime.now()
        data = str(data)
        data = data.split('-')
        self.dataInicio = f"{data[0]}-{data[1]}-01"
        self.dataFim = f"{data[0]}-{data[1]}-{data[2]}"  
    
    def createEntries(self) -> None:
        
        created_Entrie = EntriesModel.Entries(self.params).createEntriesDB()
        if(created_Entrie):
            return 'OK'
        
    def updateEntries(self) -> None:
        update_Entrie = EntriesModel.Entries(self.params).updateEntriesBD()
        if(update_Entrie):
            return 'OK'   

    def deleteEntries(self) -> None:
        delete_Entrie = EntriesModel.Entries(self.params).deleteEntriesBD()
        if(delete_Entrie):
            return 'OK'

    def getItemById(self)-> None:

                           
        getItem = EntriesModel.Entries(self.params).getItemById(self.dataInicio,self.dataFim)
        
        if(getItem != '[]'):
            return ["Ok",getItem]
    
    def getItemOnDateForFilter(self)-> None:

        getItem = EntriesModel.Entries(self.params).getItemsOnDate(self.dataInicio,self.dataFim)
        if(getItem != '[]'):
            return ["Ok",getItem]  
 
        
# params = {
#     "nome_entrada": "Salario",
#     "valor": "1000",
#     "id_user": "17",
#     "id_entries":"1"
# }

# Entrie(params).createEntries()
# Entrie(params).updateEntries()
# Entrie(params).deleteEntries()
# Entrie(params).getItemById()
