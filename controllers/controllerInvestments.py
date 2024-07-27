import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import InvestmentsModel



class Investment():
    
    def __init__(self,params) -> None:
        
       self.params = {}
       self.params = params
    def createInvestments(self) -> None:

        createdLeaves = InvestmentsModel.Investments(self.params).createInvestmentsDB()
        if(createdLeaves):
            print('Investimento Criado!!!')
        
    def updateInvestments(self) -> None:
        update_Leaves = InvestmentsModel.Investments(self.params).updateInvestmentsDB()
        if(update_Leaves):
            print("Investimento Alterado!!")    

    def deleteInvestments(self) -> None:
        delete_Leaves = InvestmentsModel.Investments(self.params).deleteInvestmentsBD()
        if(delete_Leaves):
            print("Investimento Deletado!!")
            



params = {
    "name_Investiments": "CDB",
    "type_investments": "100000",
    "value": "1",
    "profitability": "1",
    "id_user": "1",
    "id_investimentos": "1"
    
}

# Investment(params).createInvestments()
# Investment(params).updateInvestments()
Investment(params).deleteInvestments()
