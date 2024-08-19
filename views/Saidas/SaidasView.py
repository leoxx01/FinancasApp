import tkinter as tk
from tkinter import messagebox
from ttkbootstrap.constants import *
import os
import ttkbootstrap as tkk
import sys
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../controllers'))
sys.path.append(module_path)
module_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../views'))
sys.path.append(module_path2)
import controllerEntries
import controllerTypeEntries
import TelaPrincipal as TP

class Saida():

    def __init__(self,root,user,tree) -> None:
        self.janela = root
        self.tree = tree
        self.userAtual = user
        self.cadastroEntradaFinsh = ""

        
 
    def cadastroSaida(self):
        self.modal = tk.Toplevel()
        self.modal.title("Inserção de Saida/Gastos")
        self.modal.geometry("800x600")
        
        #Titulo 
        labelTitle = tkk.Label(self.modal, text="Inserção de Gastos",font=("",23))
        labelTitle.pack(pady=5)
        tkk.Separator(bootstyle="info",master=self.modal).pack(fill=X,padx=100,pady=2)

        #Tipo Gasto
        labelOpcaoSaida = tkk.Label(self.modal, text="Tipo de Gastos:")
        labelOpcaoSaida.pack(pady=2)
        entrySaida = tkk.Entry(self.modal)
        entrySaida.pack(pady=2)
        
        #Valor
        labelOpcaoGastos = tkk.Label(self.modal, text="Valor do Gasto:")
        labelOpcaoGastos.pack(pady=2)

        self.valueSlider = tkk.IntVar()
        slider = tkk.Scale(self.modal,from_=0,to=50000,variable=self.valueSlider,command=self.catchValue)
        slider.pack(pady=5)
        
        self.entryGastosIndicado = tkk.Entry(self.modal)
        self.entryGastosIndicado.pack(pady=2)
        

        labelOpcaoParcelas = tkk.Label(self.modal, text="Parcelas:")
        labelOpcaoParcelas.pack(pady=2)

        
        arrayValorParcelas = []
        for i in range(25):
            arrayValorParcelas.append(str(i))
        
        self.optionmenu_var = tkk.StringVar()
        optionmenuParcelas = tkk.OptionMenu(
                                        
                                        self.modal,
                                        self.optionmenu_var,
                                        *arrayValorParcelas,
                                        bootstyle="primary",
                                        direction="flush"
                                        )
        optionmenuParcelas.pack(pady=5)
        
        

        self.check_varPago = "Não"                             
        self.check_varPago = tkk.Checkbutton(self.modal,bootstyle="square-toggle",text="Pago ?",variable=self.check_varPago , onvalue="Sim", offvalue="Não")
        self.check_varPago.pack(pady=5)

        # Desabilita interação com a janela principal
        self.modal.transient()
        self.modal.grab_set()
        add_button = tkk.Button(self.modal, text="Inserir" ,bootstyle = "success")
        add_button.pack(pady=5)
    
        close_button = tkk.Button(self.modal, text="Fechar",bootstyle="danger" ,command=self.modal.destroy )
        close_button.pack(pady=5)

    def catchValue(self,value):
        self.entryGastosIndicado.delete(0, tkk.END)  # Primeiro, limpa o conteúdo atual
        self.entryGastosIndicado.insert(0,str(self.valueSlider.get() )) 

if __name__ == '__main__':
    root = tkk.Window()
    user = ''
    app = Saida(root,user,"")
    root.mainloop()