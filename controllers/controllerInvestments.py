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

        createdInvestiments = InvestmentsModel.Investments(self.params).createInvestmentsDB()
        if(createdInvestiments):
            print('Investimento Criado!!!')

    def readInvestments(self):
        read__Investiments = InvestmentsModel.Investiments(self.params)readInvestimentsDB()
        if(read__Investiments):
            print("Leitura de investimento concedida !!")
        
    def updateInvestments(self) -> None:
        update_Investiments = InvestmentsModel.Investments(self.params).updateInvestmentsDB()
        if(update_Investiments):
            print("Investimento Alterado!!")    

    def deleteInvestments(self) -> None:
        delete_Investiments = InvestmentsModel.Investments(self.params).deleteInvestmentsBD()
        if(delete_Investiments):
            print("Investimento Deletado!!")


params = {
    "name_Investiments": "slaoq",
    "type_investments": "2300",
    "value": "10",
    "profitability": "1",
    "id_user": "2",
    "id_investimentos": "2"
    
}

#Investment(params).createInvestments()
#Investment(params).readInvestments()
#Investment(params).updateInvestments()
#Investment(params).deleteInvestments()
