import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import InvestmentsModel



class Investment():
    
    def __init__(self,params) -> None:
        
       self.params = params
    
    def createInvestments(self) -> None:

        createdLeaves = InvestmentsModel.Investments(self.params).createInvestmentsDB()
        if(createdLeaves):
            print('Investimento Criado!!!')
        
        



params = {
    "name_Investiments": "salario",
    "type_investments": "100",
    "value": "1",
    "profitability": "1",
    "id_user": "1"
    
}

Investment(params).createInvestments()
