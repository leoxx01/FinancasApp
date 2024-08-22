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
        self.paramsEntry = paramsEntry
        self.paramsLeave = paramsLeave

        # Data da operação
        data = datetime.now()
        data = str(data)
        data = data.split('-')
        self.dataInicio = f"{data[0]}-{data[1]}-01"
        self.dataFim = f"{data[0]}-{data[1]}-{int(str(data[2])[0:2])+1}" 

        # importar as entradas
        self.receita = EntriesModel.Entries(self.paramsEntry).getItemById(self.dataInicio, self.dataFim)

        # importar as saídas
        self.gastos = LeavesModel.Leaves(self.paramsLeave).getItemById(self.dataInicio, self.dataFim)




    def desconto(self) -> None:

        receita = self.receita

        if(receita):
            print("oi")
        else:
            print("tchau")

        rec = []
        for resultados in receita:
            rec.append(float(resultados[2]))
            print(rec)

        soma = sum(rec)

        if (soma):
            print(f"Receita Liquidada! \n valor líquido: {soma}")


# dicionário com valores à serem descontados das receitas
paramsEntry = {
    "nome_entrada": "Salario",
    "valor": 1000,
    "id_user": 14,
    "id_entries": 1
}

paramsLeave = {
    "nameLeave": "carro",
    "value": 10000,
    "installments": 1,
    "pays_installments": 1,
    "pays_finish": 1,
    "id_user": 14,
    "id_leave": 2
}

processosContabeis(paramsEntry, paramsLeave).desconto()
