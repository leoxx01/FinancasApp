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

class Entrada:
    def __init__(self,root,user) -> None:
        self.janela = root
        self.userAtual = user
        
        
        
    def cadastroEntrada(self):
        
        self.janela.title("Inserção de Entrada/Lucro")
        self.janela.geometry("800x600")

        labelTitle = tkk.Label(self.janela, text="Inserção de Entrada ou Lucros",font=("",23))
        labelTitle.pack(pady=5)
        tkk.Separator(bootstyle="info",master=self.janela).pack(fill=X,padx=100,pady=2)

        labelOpcaoEntrada = tkk.Label(self.janela, text="Tipo de Entrada:")
        labelOpcaoEntrada.pack(pady=2)

        
        opcaoes = ["Salario","Salario","Aluguel","Outros"]
        self.optionmenu_var = tkk.StringVar()
        
        optionmenu = tkk.OptionMenu(
                                    self.janela,
                                    self.optionmenu_var,
                                    *opcaoes,
                                    bootstyle="primary"
                                    
                                         )
        optionmenu.pack(pady=5)
    
        
        labelOpcaoValor = tkk.Label(self.janela, text="Valor da Entrada:")
        labelOpcaoValor.pack(pady=2)

        self.valueSlider = tkk.IntVar()
        slider = tkk.Scale(self.janela,from_=0,to=50000,variable=self.valueSlider,command=self.catchValue)
        

        slider.pack(pady=5)
        

        self.entryValue = tkk.Entry(self.janela)

        self.entryValue.pack(pady=5)


        self.check_varRecorrencia = "Não"                             
        self.checkButtonEntradaRecorrente = tkk.Checkbutton(self.janela,bootstyle="square-toggle",text="Recorrente",variable=self.check_varRecorrencia , onvalue="Sim", offvalue="Não")
        self.checkButtonEntradaRecorrente.pack(pady=5)

        add_button = tkk.Button(self.janela, text="Inserir",bootstyle="success" ,command=lambda:self.insertEntrace({"nome_entrada":self.optionmenu_var.get(),"valor":self.valueSlider.get(),"id_user":self.userAtual[0][0],"id_entries":"0"}))
        add_button.pack(pady=5)
        # Desabilita interação com a janela principal
    
        close_button = tkk.Button(self.janela, text="Fechar",bootstyle="danger", command= self.leaveCadastro)

        close_button.pack(pady=5)
    def leaveCadastro(self):
        self.janela.destroy()
        root = tkk.Window()
        TP.TelaPrincipal(root,self.userAtual)
        root.mainloop()

    def EditEntrada(self):
        modal = tkk.Toplevel()
        modal.title("Edição de Entrada/Lucro")
        modal.geometry("800x600")
        
        tabview = tkk.Tabview(master=modal)
        tabview.pack(padx=20, pady=20)

        tabview.add("tab 1")  # add tab at the end
        tabview.add("tab 2")  # add tab at the end
        tabview.set("tab 2")
        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = tkk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

    def insertEntrace(self,params):
        cadastroEntradaOK = controllerEntries.Entrie(params).createEntries()
        if(cadastroEntradaOK=="OK"):
            messagebox.showinfo("Ganhos" , "Entrada de ganhos criada com sucesso!!")
            self.janela.destroy()
            root = tkk.Window()
            TP.TelaPrincipal(root,self.userAtual)
            root.mainloop()
            
        else:
            messagebox.showinfo("Ganhos" , "Algo deu Errado no cadastro!!")

    def DeleteEntrada(self):
        modal = tk.Toplevel()
        modal.title("Exclusão de Entrada/Lucro")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = tkk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
        
    def catchValue(self,value):
        self.entryValue.delete(0, tkk.END)  # Primeiro, limpa o conteúdo atual
        self.entryValue.insert(0,str(self.valueSlider.get() )) 

if __name__ == '__main__':
    root = tkk.Window()
    user = ''
    app = Entrada(root,user)
    root.mainloop()