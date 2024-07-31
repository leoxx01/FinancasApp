import tkinter as tk
from tkinter import messagebox
import customtkinter
import os
import sys
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../controllers'))
sys.path.append(module_path)
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../views/Entradas'))
sys.path.append(module_path)
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../views/Saidas'))
sys.path.append(module_path)
import EntradasView 
import SaidasView

class TelaPrincipal:
    def __init__(self,root,user) -> None:
        # criando janela
        self.janela = root
        self.janela.title("Gerenciador de finanças")
        self.janela.geometry("300x200")

        self.userAtual = user


        self.createMenu()
        self.createMain()

    def createMain(self):
        # labelTitle = customtkinter.CTkLabel(self.janela, text=f"Bem Vindo - {self.userAtual[0][1]}", fg_color="transparent",font=("",23))
        # labelTitle.pack(pady=5)
        pass
        
       
    def createMenu(self):
        self.menu_bar = tk.Menu(self.janela)

        self.entradaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Entrada", menu=self.entradaMenu)
        self.entradaMenu.add_command(label="Cadastrar" ,command=EntradasView.Entrada(self.janela,self.userAtual).cadastroEntrada)
        self.entradaMenu.add_separator()
        self.entradaMenu.add_command(label="Editar" ,command=EntradasView.Entrada(self.janela,self.userAtual).EditEntrada)
        self.entradaMenu.add_separator()
        self.entradaMenu.add_command(label="Excluir" ,command=EntradasView.Entrada(self.janela,self.userAtual).DeleteEntrada)
        
        
        self.saidaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Gastos", menu=self.saidaMenu)
        self.saidaMenu.add_command(label="Cadastrar" ,command=SaidasView.Saida(self.janela,self.userAtual).cadastroSaida)
        self.saidaMenu.add_separator()
        self.saidaMenu.add_command(label="Editar" ,command=SaidasView.Saida(self.janela,self.userAtual).editSaida)
        self.saidaMenu.add_separator()
        self.saidaMenu.add_command(label="Excluir" ,command=SaidasView.Saida(self.janela,self.userAtual).deleteSaida)

        self.financaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Investimentos", menu=self.financaMenu)
        self.financaMenu.add_command(label="Cadastrar" ,command=self.cadastroInvestimentos)
        self.financaMenu.add_separator()
        self.financaMenu.add_command(label="Editar" ,command=self.editInvestimentos)
        self.financaMenu.add_separator()
        self.financaMenu.add_command(label="Excluir" ,command=self.deleteInvestimentos)

        self.janela.config(menu=self.menu_bar)

    def cadastroInvestimentos(self):
        modal = tk.Toplevel()
        modal.title("Inserção de Investimento")
        modal.geometry("800x600")

        labelTitle = customtkinter.CTkLabel(modal, text="Inserção de Investimentos", fg_color="transparent",font=("",23))
        labelTitle.pack(pady=5)

        labelNomeInvestmento = customtkinter.CTkLabel(modal,text="Nome do Investimento:")
        labelNomeInvestmento.pack(pady = 5 )
        entryNomeInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Nome Investimento")
        entryNomeInvestimento.pack(pady=5)

        labelTipoInvestmento = customtkinter.CTkLabel(modal,text="Tipo do Investimento:")
        labelTipoInvestmento.pack(pady = 5 )
        entryTipoInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Tipo Investimento")
        entryTipoInvestimento.pack(pady=5)
        
        labelValorInvestmento = customtkinter.CTkLabel(modal,text="Valor do Investimento:")
        labelValorInvestmento.pack(pady = 5 )
        entryValorInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Valor Investimento")
        entryValorInvestimento.pack(pady=5)

        labelRentabilidadeInvestmento = customtkinter.CTkLabel(modal,text="Rentabilidade do Investimento:")
        labelRentabilidadeInvestmento.pack(pady = 5 )
        entryRentabilidadeInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Rentabilidade Investimento")
        entryRentabilidadeInvestimento.pack(pady=5)

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        add_button = customtkinter.CTkButton(modal, text="Inserir" )
        add_button.pack(pady=5)

        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
    
    def editInvestimentos(self):
        modal = tk.Toplevel()
        modal.title("Edição de Investimento")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
    
    def deleteInvestimentos(self):
        modal = tk.Toplevel()
        modal.title("Exclusão de Investimento")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

    
if __name__ == '__main__':
    root = customtkinter.CTk()
    user = ''
    app = TelaPrincipal(root,user)
    root.mainloop()