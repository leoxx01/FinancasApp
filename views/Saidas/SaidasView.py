import tkinter as tk
from tkinter import messagebox
import customtkinter
import os
import sys
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../controllers'))
sys.path.append(module_path)
module_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../views'))
sys.path.append(module_path2)
import controllerLeave
import TelaPrincipal as TP

class Saida():

    def __init__(self,root,user) -> None:
        self.janela = root
        self.userAtual = user
        
 
    def cadastroSaida(self):
        modal = tk.Toplevel()
        modal.title("Inserção de Saida/Gastos")
        modal.geometry("800x600")
        labelTitle = customtkinter.CTkLabel(modal, text="Inserção de Saida/Gastos", fg_color="transparent",font=("",23))
        labelTitle.pack(pady=5)
        labelOpcaoSaida = customtkinter.CTkLabel(modal, text="Tipo de Gastos:", fg_color="transparent")
        labelOpcaoSaida.pack(pady=2)
        entrySaida = customtkinter.CTkEntry(modal, placeholder_text="Nome do Gasto")
        entrySaida.pack(pady=2)
        labelOpcaoGastos = customtkinter.CTkLabel(modal, text="Valor Gasto:", fg_color="transparent")
        labelOpcaoGastos.pack(pady=2)
        entryGastosIndicado = customtkinter.CTkEntry(modal, placeholder_text="Indique o valor Gasto")
        entryGastosIndicado.pack(pady=2)
        
        labelOpcaoParcelas = customtkinter.CTkLabel(modal, text="Parcelas:", fg_color="transparent")
        labelOpcaoParcelas.pack(pady=2)
        optionmenu_var = customtkinter.StringVar()
        arrayValorParcelas = []
        for i in range(25):
            arrayValorParcelas.append(str(i))
        
        optionmenuParcelas = customtkinter.CTkOptionMenu(modal,values=arrayValorParcelas,
                                        variable=optionmenu_var)
        optionmenuParcelas.pack(pady=5)
        
        labelPago = customtkinter.CTkLabel(modal, text="Indique o status de pagamento", fg_color="transparent")
        labelPago.pack(pady=2)
        switch_var = customtkinter.StringVar(value="Sim")
        switch = customtkinter.CTkSwitch(modal, text="Já está pago?",
                                variable=switch_var, onvalue="Sim", offvalue="Não")
        switch.pack(pady=2)
        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        add_button = customtkinter.CTkButton(modal, text="Inserir" )
        add_button.pack(pady=5)
    
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy )
        close_button.pack(pady=5)
    
    def editSaida(self):
        modal = tk.Toplevel()
        modal.title("Edição de Saida/Gastos")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

    def deleteSaida(self):
        modal = tk.Toplevel()
        modal.title("Exclusão de Saida/Gastos")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()

if __name__ == '__main__':
    root = customtkinter.CTk()
    user = ''
    app = Saida(root,user)
    root.mainloop()