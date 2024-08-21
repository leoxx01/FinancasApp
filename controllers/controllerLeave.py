import sys
import os
from datetime import datetime
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import LeavesModel



class Leave():
    
    def __init__(self,params) -> None:
        
        self.params = params

        data = datetime.now()
        data = str(data)
        data = data.split('-')
        self.dataInicio = f"{data[0]}-{data[1]}-01"
        self.dataFim = f"{data[0]}-{data[1]}-{int(str(data[2])[0:2])+1}" 
    
    def createLeaves(self) -> None:

        created_Leaves = LeavesModel.Leaves(self.params).createLeavesDB()
        if(created_Leaves):
            print('Saida Criada!!!')

    def updateLeaves(self) -> None:
        update_Leaves = LeavesModel.Leaves(self.params).updateLeavesBD()
        if(update_Leaves):
            print("Saida Alterada!!")    

    def deleteLeaves(self) -> None:
        delete_Leaves = LeavesModel.Leaves(self.params).deleteLeavesBD(self.dataInicio,self.dataFim)
        if(delete_Leaves):
            print("Saida Deletada!!")
    def getItemById(self) -> None:
        getItem = LeavesModel.Leaves(self.params).getItemById(self.dataInicio,self.dataFim)
        if(getItem != '[]'):
            return ["Ok",getItem]
    

params = {
    "nameLeave": "carro",
    "value": "10000",
    "installments": "1",
    "pays_installments": "1",
    "pays_finish": "1",
    "id_user": "1",
    "id_leave": "1"
    
}

# Leave(params).createLeaves()
# Leave(params).updateLeaves()
# Leave(params).deleteLeaves()
