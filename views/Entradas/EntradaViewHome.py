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
import TelaPrincipal as TP
import EntradasView

class EntradaHomeView():

    def __init__(self,root,user) -> None:
        self.janela = root
        self.userAtual = user
        self.janela.title("Gerenciador de finanças")
        self.janela.geometry("300x200")
        
        # self.loadInformations()
    
    def loadInformations(self):
        
        # buttonbar = tkk.Frame(self.janela,style='primary.TFrame')
        # buttonbar.pack(fill=X,  side=TOP)

        # btnReceita = tkk.Button(master=buttonbar, text='Receita')
        # btnReceita.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        # btnGastos = tkk.Button(master=buttonbar, text='Gastos')
        # btnGastos.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        # btnInvestimentos = tkk.Button(master=buttonbar, text='Investimentos')
        # btnInvestimentos.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1) 

        left_panel = tkk.Frame(self.janela, style='info.TFrame')
        left_panel.pack(side=LEFT, fill=Y)
        
        
        
        selfAddReceita = tkk.Button(left_panel,bootstyle="info",text="Adcionar Receita",command= EntradasView.Entrada(self.janela,self.userAtual).cadastroEntrada)
        selfAddReceita.pack(pady=5)

        selfAddCategoria = tkk.Button(left_panel,bootstyle="info",text="Adcionar Categotia",command=EntradasView.Entrada(self.janela,"").cadastroEntrada)
        selfAddCategoria.pack(pady=5)

        central_panel = tkk.Frame(self.janela, style='TFrame')
        central_panel.pack(fill=Y,pady=5)

        labelDataEntrada = tkk.Label(central_panel,text="Data Inicio :",bootstyle="info")
        labelDataEntrada.pack(pady=5,side=LEFT)
        filterDataEntrada = tkk.DateEntry(central_panel,bootstyle="info")
        filterDataEntrada.pack(pady= 1,padx=10,side=LEFT)

        labelDataFim = tkk.Label(central_panel,text="Data Inicio :",bootstyle="info")
        labelDataFim.pack(pady=5,side=LEFT)
        filterDataFim = tkk.DateEntry(central_panel,bootstyle="info")
        filterDataFim.pack(pady= 1,padx=10,side=LEFT)

        buttonFiltrar = tkk.Button(central_panel,bootstyle="info",text="Filtrar")
        buttonFiltrar.pack(side=LEFT)


        data = [
                ("1", "Salario", "10000"),
                ("2", "Alugel", "500"),
                ("3", "Outros", "150")
            ]
        self.tree = tkk.Treeview(self.janela, columns=("ID", "Tipo Receita", "Valor"), show="headings", height=10,bootstyle='info')
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Tipo Receita", width=200, anchor=tk.CENTER)
        self.tree.column("Valor", width=300, anchor=tk.CENTER)
        


        self.tree.heading("ID", text="ID")
        self.tree.heading("Tipo Receita", text="Tipo Receita")
        self.tree.heading("Valor", text="Valor(R$)")
        

        for item in data:
            self.tree.insert("", "end", values=item)
            

        self.tree.pack(fill=tk.BOTH,padx=10,pady=5)


        self.tree.bind("<Double-1>",self.editItem)

    def editItem(self,event):
        selected_item = self.tree.focus()
        item_values = self.tree.item(selected_item, "values")

        EntradasView.Entrada(self.janela,"").EditEntrada(item_values)

if __name__ == '__main__':
    root = tkk.Window()
    user = ''
    app = EntradaHomeView(root,user)
    root.mainloop()