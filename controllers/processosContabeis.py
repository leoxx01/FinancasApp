import sys
import os
from datetime import datetime

# import path do modal
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)

import EntriesModel
import LeavesModel


class processosContabeis:
    def __init__(self, paramsEntry, paramsLeave) -> None:
        self.receita = paramsEntry
        self.custos = paramsLeave

        ###  Esta aplicação só poderá ser ligada ao modal, quando as saídas estiverem prontas !!!

#        # Data da operação
#        data = datetime.now()
#        data = str(data)
#        data = data.split('-')
#        self.dataInicio = f"{data[0]}-{data[1]}-01"
#        self.dataFim = f"{data[0]}-{data[1]}-{int(str(data[2])[0:2])+1}" 
#
#        # importar as entradas
#        self.receita = EntriesModel.Entries(self.paramsEntry).getItemById(self.dataInicio, self.dataFim)
#
#        # importar as saídas
#        self.gastos = LeavesModel.Leaves(self.paramsLeave).getItemById(self.dataInicio, self.dataFim)

        
    def desconto(self) -> None:

        receita = self.receita
        custos = self.custos

        print(receita[0]['valor'])
        print(custos[0]['value'])

        print('\n')

        # total receitas
        rec = []
        for valores in receita:
            cont = 0
            rec.append(float(valores['valor']))
            cont += 1
        
        receitaTotal = sum(rec)
        print(receitaTotal)

        # total custos
        cus = []
        for valores in custos:
            cont = 0
            cus.append(float(valores['value']))
            cont += 1
        
        custoTotal = sum(cus)
        print(custoTotal)

        # desconto final
        

# dicionário com valores à serem descontados das receitas (exemplo)
paramsEntry = [
        {
        "nome_entrada": "Salario",
        "valor": 1000,
        "id_user": 14,
        "id_entries": 1
    },
        {
        "nome_entrada": "Salario",
        "valor": 1030,
        "id_user": 14,
        "id_entries": 1
    }
]
paramsLeave = [
        {
        "nameLeave": "carro",
        "value": 10000,
        "installments": 1,
        "pays_installments": 1,
        "pays_finish": 1,
        "id_user": 14,
        "id_leave": 2
    },
        {
        "nameLeave": "carro",
        "value": 2000,
        "installments": 1,
        "pays_installments": 1,
        "pays_finish": 1,
        "id_user": 14,
        "id_leave": 2
    }
]

processosContabeis(paramsEntry, paramsLeave).desconto()
