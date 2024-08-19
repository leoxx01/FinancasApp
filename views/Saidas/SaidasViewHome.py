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
import SaidasView
import controllerTypeEntries
import TypeEntradaView
from ttkbootstrap.widgets import DateEntry
from ttkbootstrap.constants import *

class SaidaHomeView():
    def __init__(self,root,user) -> None:
        
        self.janela = root
        self.userAtual = user
        self.janela.title("Gerenciador de finanças")
        self.janela.geometry("1200x900")

        
    def loadInformations(self):
        #Menu Lateral

        self.left_panel_gasto = tkk.Frame(self.janela, style='info.TFrame')
        self.left_panel_gasto.pack(side=LEFT, fill=Y)
        
        selfAddGasto = tkk.Button(self.left_panel_gasto,bootstyle="info",text="Adcionar Gasto",command= self.casdastroGastoButton)
        selfAddGasto.pack(pady=5)

        selfAddCategoria = tkk.Button(self.left_panel_gasto,bootstyle="info",text="Adcionar Categotia",command=print(''))
        selfAddCategoria.pack(pady=5)

        #Painel Inicio com filtros
        self.central_panel = tkk.Frame(self.janela, style='TFrame')
        self.central_panel.pack(fill=Y,pady=5)

        labelDataEntrada = tkk.Label(self.central_panel,text="Data Inicio :",bootstyle="info")
        labelDataEntrada.pack(pady=5,side=LEFT)
        self.filterDataEntrada = tkk.DateEntry(self.central_panel,bootstyle="info",dateformat="%Y-%m-%d")
        self.filterDataEntrada.pack(pady= 1,padx=10,side=LEFT)

        labelDataFim = tkk.Label(self.central_panel,text="Data Fim :",bootstyle="info")
        labelDataFim.pack(pady=5,side=LEFT)
        self.filterDataFim = tkk.DateEntry(self.central_panel,bootstyle="info", dateformat="%Y-%m-%d")
        self.filterDataFim.pack(pady= 1,padx=10,side=LEFT)

        # opcaoesNew = controllerTypeEntries.TypeEntriesController({"nameEntrie":""}).selectAllTypeEntries()

        self.tipoReceitaFilter = tkk.Menubutton(self.central_panel,text="Categoria",bootstyle="info")
        self.tipoReceitaFilter.pack(pady= 1,padx=10,side=LEFT)

        menu = tkk.Menu(self.tipoReceitaFilter, tearoff=0)
        self.tipoReceitaFilter.config(menu=menu)
          
        # for i in opcaoesNew:
        #     menu.add_command(label=i[0], command=lambda opt=i[0]: self.catchTipoReceita(opt))

        buttonFiltrar = tkk.Button(self.central_panel,bootstyle="info",text="Filtrar",command = lambda: self.catchData())
        buttonFiltrar.pack(side=LEFT)
        #Termina Filtros

        #Carrega Dados
        # data2  = controllerEntries.Entrie({"nome_entrada":"","valor":"","id_user":str(self.userAtual),"id_entries":""}).getItemById()

        #Monta Schema Tree
        self.treeGastos = tkk.Treeview(self.janela, columns=("ID", "Tipo de Gasto", "Valor"), show="headings", height=10,bootstyle='info')
        self.treeGastos.column("ID", width=50, anchor=tk.CENTER)
        self.treeGastos.column("Tipo de Gasto", width=200, anchor=tk.CENTER)
        self.treeGastos.column("Valor", width=300, anchor=tk.CENTER)
    
        self.treeGastos.heading("ID", text="ID")
        self.treeGastos.heading("Tipo de Gasto", text="Tipo de Gasto")
        self.treeGastos.heading("Valor", text="Valor(R$)")
        
        #Inicia Vars de informações 
        mediaReceita = 0
        maiorreceita = 0
        menorReceita = -1

        #Monta tree com dados pegos do banco de dados
        # for item in data2[1]:
        #     self.treeGastos.insert("", "end", values=(item[0],item[1],item[2]))
        #     mediaReceita += int(item[2])
        #     if(menorReceita == -1):
        #         menorReceita = int(item[2])

        #     if(int(item[2]) > int(maiorreceita)):
        #         maiorreceita = float(item[2])
        #     elif(int(item[2]) < int(menorReceita)):
        #         menorReceita = float(item[2])
            

        self.treeGastos.pack(fill=tk.BOTH,padx=10,pady=5)
        
        #Bind para o double clique iniciar o modo edição
        self.treeGastos.bind("<Double-1>",self.editItem)

        #Fim Tree

        #Inicio Painel que apresenta informações
        self.infos_panel = tkk.Frame(self.janela, style='TFrame')
        self.infos_panel.pack(fill=Y,pady=5)

        self.MaiorReceitaFrame =  tkk.Labelframe(self.infos_panel,bootstyle="success",text="Maior Gasto")
        selfMaiorReceita = tkk.Label(self.MaiorReceitaFrame,font='bold',text=f"R$ {format(maiorreceita,".2f")}")
        selfMaiorReceita.pack()
        self.MaiorReceitaFrame.pack(side=LEFT,padx=5)
        
        self.MediaReceitaFrame =  tkk.Labelframe(self.infos_panel,bootstyle="warning",text="Gasto Media")
        selfMediaReceita = tkk.Label(self.MediaReceitaFrame,font='bold',text=f"R$ 0,00")#{format(mediaReceita/len(data2),'.2f')}
        selfMediaReceita.pack()
        self.MediaReceitaFrame.pack(side=LEFT,padx=5)

        self.MenorReceitaFrame =  tkk.Labelframe(self.infos_panel,bootstyle="danger",text="Menor Gasto")
        selfMenorReceita = tkk.Label(self.MenorReceitaFrame,font='bold',text=f"R$ {format(menorReceita,'.2f')}")
        selfMenorReceita.pack()
        self.MenorReceitaFrame.pack(side=LEFT,padx=5)
        
        return[self.left_panel_gasto,self.treeGastos,self.central_panel,self.infos_panel]
    
    def casdastroGastoButton(self):
        SaidasView.Saida(self.janela,self.userAtual,self.treeGastos).cadastroSaida()

    def editItem(self):
        pass

if __name__ == '__main__':
    root = tkk.Window()
    user = ''
    app = SaidaHomeView(root,user)
    root.mainloop()