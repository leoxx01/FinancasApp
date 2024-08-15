import tkinter as tk
from tkinter import messagebox
from ttkbootstrap.constants import *
import customtkinter
import os
import sys
import ttkbootstrap as tkk

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../controllers'))
sys.path.append(module_path)
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../views/Entradas'))
sys.path.append(module_path)
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../views/Saidas'))
sys.path.append(module_path)
import EntradaViewHome
import SaidasViewHome

class TelaPrincipal:
    def __init__(self,root,user) -> None:
        # criando janela
        
        self.tela = ""
        self.janela = root
        
        self.janela.title("Gerenciador de finanças")
        self.janela.geometry("300x200")

        self.userAtual = user
        
        print(user)
        
        self.createMenu()
        self.createMain()
        
        self.varsDemontaEntrada = ''
        self.varsDemontaGasto = ''



    def createMain(self):
        # labelTitle = tkk.Label(self.janela, text=f"Bem Vindo - {self.userAtual[0][1]}", font=("",23))
        # labelTitle.pack(pady=5)
        pass
        
       
    def createMenu(self):
        buttonbar = tkk.Frame(self.janela,style='primary.TFrame')
        buttonbar.pack(fill=X, pady=1, side=TOP)

        btnReceita = tkk.Button(master=buttonbar, text='💲 Receita' , command=self.callEntries)
        btnReceita.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        btnGastos = tkk.Button(master=buttonbar, text='💸 Gastos',command=self.callGastos)
        btnGastos.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        btnInvestimentos = tkk.Button(master=buttonbar, text='📈 Investimentos')
        btnInvestimentos.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        
        menuButton = tkk.Menubutton(buttonbar,text=f'👤 {self.userAtual[0][1]}')
        menuButton.pack(pady= 1,padx=10,side=RIGHT)

        menu = tkk.Menu(menuButton, tearoff=0)
        
        menuButton.config(menu=menu)

        menu.add_command(label="Perfil", command=print('oi'))
        menu.add_command(label="Logout", command=print('oi'))
        menu.add_command(label="Sair", command= print('oi'))

        menuButtonLingua = tkk.Menubutton(buttonbar,text=f'🌎 Linguagem')
        menuButtonLingua.pack(pady= 1,padx=10,side=RIGHT)

        menu2 = tkk.Menu(menuButtonLingua, tearoff=0)
        
        menuButtonLingua.config(menu=menu2)

        menu2.add_command(label="PT-BR", command=print('oi'))
        menu2.add_command(label="EN", command= print('oi'))
        menu2.add_command(label="ES", command= print('oi'))
       
    def callEntries(self):
        
        if(self.tela == "" or self.tela != 'Entrada'):
            self.limpaTela()
            self.varsDemontaEntrada = EntradaViewHome.EntradaHomeView(self.janela,self.userAtual).loadInformations()
            self.tela = 'Entrada'
            
    def callGastos(self):

        if(self.tela == "" or self.tela != 'Gastos'):
            self.limpaTela()
            self.varsDemontaGasto = SaidasViewHome.SaidaHomeView(self.janela,self.userAtual).loadInformations()
            self.tela = 'Gastos'
            
     
    def limpaTela(self):

        if(len(self.varsDemontaEntrada) > 0):
            for i in self.varsDemontaEntrada:
                    i.destroy()
        if(len(self.varsDemontaGasto) > 0):
             for i in self.varsDemontaGasto:
                    i.destroy()

    def cadastroInvestimentos(self):
        modal = tkk.Toplevel()
        modal.title("Inserção de Investimento")
        modal.geometry("800x600")

        labelTitle = tkk.Label(modal, text="Inserção de Investimentos", font=("",23))
        labelTitle.pack(pady=5)

        labelNomeInvestmento = tkk.Label(modal,text="Nome do Investimento:")
        labelNomeInvestmento.pack(pady = 5 )
        entryNomeInvestimento = tkk.Entry(modal,placeholder_text="Nome Investimento")
        entryNomeInvestimento.pack(pady=5)

        labelTipoInvestmento = tkk.Label(modal,text="Tipo do Investimento:")
        labelTipoInvestmento.pack(pady = 5 )
        entryTipoInvestimento = tkk.Entry(modal,placeholder_text="Tipo Investimento")
        entryTipoInvestimento.pack(pady=5)
        
        labelValorInvestmento = tkk.Label(modal,text="Valor do Investimento:")
        labelValorInvestmento.pack(pady = 5 )
        entryValorInvestimento = tkk.Entry(modal,placeholder_text="Valor Investimento")
        entryValorInvestimento.pack(pady=5)

        labelRentabilidadeInvestmento = tkk.Label(modal,text="Rentabilidade do Investimento:")
        labelRentabilidadeInvestmento.pack(pady = 5 )
        entryRentabilidadeInvestimento = tkk.Entry(modal,placeholder_text="Rentabilidade Investimento")
        entryRentabilidadeInvestimento.pack(pady=5)

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        add_button = tkk.Button(modal, text="Inserir" )
        add_button.pack(pady=5)

        close_button = tkk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
    
    def editInvestimentos(self):
        modal = tkk.Toplevel()
        modal.title("Edição de Investimento")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = tkk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
    
    def deleteInvestimentos(self):
        modal = tkk.Toplevel()
        modal.title("Exclusão de Investimento")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = tkk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

    
if __name__ == '__main__':
    
    root = tkk.Window()
    user = ''
    app = TelaPrincipal(root,user)
    root.mainloop()