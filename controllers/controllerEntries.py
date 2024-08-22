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
        self.dataFim = f"{data[0]}-{data[1]}-{int(str(data[2])[0:2])+1}" 


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
            return 'OK'   

    def deleteEntries(self) -> None:
        delete_Entrie = EntriesModel.Entries(self.params).deleteEntriesBD()
        if(delete_Entrie):
            return 'OK'

    def getItemById(self)-> None:

        getItem = EntriesModel.Entries(self.params).getItemById(self.dataInicio,self.dataFim)
                
        if(getItem != '[]'):
            print(getItem)
            return ["Ok",getItem]
    
    def getItemOnDateForFilter(self,dtInicioProc,dtFimProc)-> None:
        dtFimProcSplit = dtFimProc.split('-')
        dtFimProc = f"{dtFimProcSplit[0]}-{dtFimProcSplit[1]}-{int(dtFimProcSplit[2])+1}"

        getItem = EntriesModel.Entries(self.params).getItemsOnDate(dtInicioProc,dtFimProc)
        if(getItem != '[]'):
            return ["Ok",getItem]  


params = {
    "nome_entrada": "Salario",
    "valor": 1000,
    "id_user": 17,
    "id_entries":1
}


# Entrie(params).createEntries()
# Entrie(params).readEntries()
# Entrie(params).updateEntries()
# Entrie(params).deleteEntries()
Entrie(params).getItemById()
