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
from ttkbootstrap.constants import *

class EntradaHomeView():

    def __init__(self,root,user) -> None:
        self.janela = root
        print(user)
        self.userAtual = user[0][0]
        self.janela.title("Gerenciador de finanças")
        self.janela.geometry("300x200")
        
   

    def loadInformations(self):
    
        #Menu Lateral
        left_panel = tkk.Frame(self.janela, style='info.TFrame')
        left_panel.pack(side=LEFT, fill=Y)
        
        selfAddReceita = tkk.Button(left_panel,bootstyle="info",text="Adcionar Receita",command= self.casdastroEntradaButton)
        selfAddReceita.pack(pady=5)

        selfAddCategoria = tkk.Button(left_panel,bootstyle="info",text="Adcionar Categotia",command=EntradasView.Entrada(self.janela,"","").cadastroEntrada)
        selfAddCategoria.pack(pady=5)

        #Fim Menu Lateral

        #Painel Inicio com filtros
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

        tipoReceitaFilter = tkk.Menubutton(central_panel,text="Tipo de Receita",bootstyle="info")
        tipoReceitaFilter.pack(pady= 1,padx=10,side=LEFT)

        buttonFiltrar = tkk.Button(central_panel,bootstyle="info",text="Filtrar")
        buttonFiltrar.pack(side=LEFT)

        #Fim panel filtros
        
        #Inicio Tree para trazer dados

        #Carrega Dados
        data2  = controllerEntries.Entrie({"nome_entrada":"","valor":"","id_user":str(self.userAtual),"id_entries":""}).getItemById()

        #Monta Schema Tree
        self.tree = tkk.Treeview(self.janela, columns=("ID", "Tipo Receita", "Valor"), show="headings", height=10,bootstyle='info')
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Tipo Receita", width=200, anchor=tk.CENTER)
        self.tree.column("Valor", width=300, anchor=tk.CENTER)
    
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tipo Receita", text="Tipo Receita")
        self.tree.heading("Valor", text="Valor(R$)")
        
        #Inicia Vars de informações 
        mediaReceita = 0
        maiorreceita = 0
        menorReceita = -1

        #Monta tree com dados pegos do banco de dados
        for item in data2[1]:
            self.tree.insert("", "end", values=(item[0],item[1],item[2]))
            mediaReceita += int(item[2])
            if(menorReceita == -1):
                menorReceita = int(item[2])

            if(int(item[2]) > int(maiorreceita)):
                maiorreceita = float(item[2])
            elif(int(item[2]) < int(menorReceita)):
                menorReceita = float(item[2])
            

        self.tree.pack(fill=tk.BOTH,padx=10,pady=5)
        
        #Bind para o double clique iniciar o modo edição
        self.tree.bind("<Double-1>",self.editItem)

        #Fim da Tree

        #Inicio Painel que apresenta informações
        infos_panel = tkk.Frame(self.janela, style='TFrame')
        infos_panel.pack(fill=Y,pady=5)

        self.MaiorReceitaFrame =  tkk.Labelframe(infos_panel,bootstyle="success",text="Maior receita")
        selfMaiorReceita = tkk.Label(self.MaiorReceitaFrame,font='bold',text=f"R$ {format(maiorreceita,".2f")}")
        selfMaiorReceita.pack()
        self.MaiorReceitaFrame.pack(side=LEFT,padx=5)
        
        self.MediaReceitaFrame =  tkk.Labelframe(infos_panel,bootstyle="warning",text="Receita Media")
        selfMediaReceita = tkk.Label(self.MediaReceitaFrame,font='bold',text=f"R$ {format(mediaReceita/len(data2),'.2f')}")
        selfMediaReceita.pack()
        self.MediaReceitaFrame.pack(side=LEFT,padx=5)

        self.MenorReceitaFrame =  tkk.Labelframe(infos_panel,bootstyle="danger",text="Menor Receita")
        selfMenorReceita = tkk.Label(self.MenorReceitaFrame,font='bold',text=f"R$ {format(menorReceita,'.2f')}")
        selfMenorReceita.pack()
        self.MenorReceitaFrame.pack(side=LEFT,padx=5)

        #Fim painel
    def casdastroEntradaButton(self):
        statusEntrada = EntradasView.Entrada(self.janela,self.userAtual,self.tree ).cadastroEntrada()
        print(statusEntrada)
        if(statusEntrada):
            pass
        
    def editItem(self,event):
        selected_item = self.tree.focus()
        item_values = self.tree.item(selected_item, "values")

        EntradasView.Entrada(self.janela,"").EditEntrada(item_values)

if __name__ == '__main__':
    root = tkk.Window()
    user = ''
    app = EntradaHomeView(root,user)
    root.mainloop()