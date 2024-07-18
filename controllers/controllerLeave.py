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

    def updateLeaves(self) -> None:
        update_Leaves = LeavesModel.Leaves(self.params).updateLeavesBD()
        if(update_Leaves):
            print("Saida Alterada!!")    

    def deleteLeaves(self) -> None:
        delete_Leaves = LeavesModel.Leaves(self.params).deleteLeavesBD()
        if(delete_Leaves):
            print("Saida Deletada!!")
        
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
