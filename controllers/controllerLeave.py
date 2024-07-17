import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import LeavesModel



class Leave():
    
    def __init__(self,params) -> None:
        
       self.params = params
    
    def createLeaves(self) -> None:

        createdLeaves = LeavesModel.Leaves(self.params).createLeavesDB()
        if(createdLeaves):
            print('Saida Criada!!!')
        
params = {
    "nameLeave": "salario",
    "value": "100",
    "installments": "1",
    "pays_installments": "1",
    "pays_finish": "1",
    "id_user": "1"
    
}

Leave(params).createLeaves()
