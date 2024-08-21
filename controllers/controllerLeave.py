import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import LeavesModel

class Leave():
    
    def __init__(self,params) -> None:
        
       self.params = params
    
    def createLeaves(self) -> None:
        created_Leaves = LeavesModel.Leaves(self.params).createLeavesDB()
        if(created_Leaves):
            print('Saida Criada!!!')

    def readLeaves(self):
        read_Leaves = LeavesModel.Leaves(self.params).readLeavesDB()

        for resultados in read_Leaves:
            print(resultados)

        if(read_Leaves):
            print("leitura de saída concedida !!")

    def updateLeaves(self) -> None:
        update_Leaves = LeavesModel.Leaves(self.params).updateLeavesBD()
        if(update_Leaves):
            print("Saida Alterada!!")    

    def deleteLeaves(self) -> None:
        delete_Leaves = LeavesModel.Leaves(self.params).deleteLeavesBD()
        if(delete_Leaves):
            print("Saida Deletada!!")
        
    def getItemById(self) -> dict:
        getItem = LeavesModel.Leaves(self.params).getItemById()
        
        if(getItem != []):
            print("Ok !", getItem[0][2])
            return getItem

params = {
    "nameLeave": "carro",
    "value": 10000,
    "installments": 1,
    "pays_installments": 1,
    "pays_finish": 1,
    "id_user": 14,
    "id_leave": 2
}

# Leave(params).createLeaves()
# Leave(params).readLeaves()
# Leave(params).updateLeaves()
# Leave(params).deleteLeaves()
Leave(params).getItemById()
