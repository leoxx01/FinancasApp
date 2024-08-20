import sys
import os

# import path do modal
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)

import EntriesModel
import LeavesModel


class processosContabeis:
    def __init__(self, params) -> None:
        self.params = params
        
        # importar as entradas
        self.receita = EntriesModel.Entries(self.params).getItemById()

        # importar as saídas
        #self.gastos = LeavesModel.Leaves(self.params).#getItemById()


    def desconto(self) -> None:

        receita = self.receita

        rec = []
        for resultados in receita:
            rec.append(float(resultados[2]))
            print(rec)
            
        soma = sum(rec)

        if (soma):
            print(f"Receita Liquidada! \n valor líquido: {soma}")


# dicionário com valores à serem descontados das receitas
params = {
    "nome_entrada": "Salario",
    "valor": 1000,
    "id_user": 14,
    "id_entries": 1
}

processosContabeis(params).desconto()