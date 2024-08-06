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
        self.modal = tkk.Toplevel()
        self.modal.title("Inserção de Entrada/Lucro")
        
        self.modal.geometry("800x600")

        labelTitle = tkk.Label(self.modal, text="Inserção de Entrada ou Lucros",font=("",23))
        labelTitle.pack(pady=5)
        tkk.Separator(bootstyle="info",master=self.modal).pack(fill=X,padx=100,pady=2)

        labelOpcaoEntrada = tkk.Label(self.modal, text="Tipo de Entrada:")
        labelOpcaoEntrada.pack(pady=2)

        
        opcaoes = ["Salario","Salario","Aluguel","Outros"]
        self.optionmenu_var = tkk.StringVar()
        
        optionmenu = tkk.OptionMenu(
                                    self.modal,
                                    self.optionmenu_var,
                                    *opcaoes,
                                    bootstyle="primary"
                                    
                                         )
        optionmenu.pack(pady=5)
    
        
        labelOpcaoValor = tkk.Label(self.modal, text="Valor da Entrada:")
        labelOpcaoValor.pack(pady=2)

        self.valueSlider = tkk.IntVar()
        slider = tkk.Scale(self.modal,from_=0,to=50000,variable=self.valueSlider,command=self.catchValue)
        

        slider.pack(pady=5)
        

        self.entryValue = tkk.Entry(self.modal)

        self.entryValue.pack(pady=5)


        self.check_varRecorrencia = "Não"                             
        self.checkButtonEntradaRecorrente = tkk.Checkbutton(self.modal,bootstyle="square-toggle",text="Recorrente",variable=self.check_varRecorrencia , onvalue="Sim", offvalue="Não")
        self.checkButtonEntradaRecorrente.pack(pady=5)

        self.modal.transient()
        self.modal.grab_set()
        

        add_button = tkk.Button(self.modal, text="Inserir",bootstyle="success" ,command=lambda:self.insertEntrace({"nome_entrada":self.optionmenu_var.get(),"valor":self.valueSlider.get(),"id_user":self.userAtual[0][0],"id_entries":"0"}))
        add_button.pack(pady=5)
        # Desabilita interação com a janela principal
    
        close_button = tkk.Button(self.modal, text="Fechar",bootstyle="danger", command= self.modal.destroy)

        close_button.pack(pady=5)


    def EditEntrada(self,item_values):
        modal = tkk.Toplevel()
        modal.title("Edição de Entrada/Lucro")
        modal.geometry("800x600")

        labelTitle = tkk.Label(modal, text="Edição | Exclusão de Receita",font=("",23))
        labelTitle.pack(pady=5)
        tkk.Separator(bootstyle="info",master=modal).pack(fill=X,padx=100,pady=2)

        print(item_values)
        
        

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        labelReceita = tkk.Label(modal,text="Tipo de Receita").pack()
        self.tipoReceita = tkk.Entry(modal)
        self.tipoReceita.pack()
        labelValor = tkk.Label(modal,text="Valor").pack()
        self.valorReceita = tkk.Entry(modal)
        self.valorReceita.pack()
        
        self.tipoReceita.delete(0, tkk.END)  
        self.tipoReceita.insert(0,str(item_values[1])) 
        self.valorReceita.delete(0, tkk.END)  
        self.valorReceita.insert(0,str(item_values[2])) 

        editButton = tkk.Button(modal,text="Atualizar",bootstyle="info-outline").pack(pady=5)
        deleteButton = tkk.Button(modal,text="Deletar",bootstyle="danger-outline").pack(pady=5)
        
   
       

    def insertEntrace(self,params):
        cadastroEntradaOK = controllerEntries.Entrie(params).createEntries()
        if(cadastroEntradaOK=="OK"):
            messagebox.showinfo("Ganhos" , "Entrada de ganhos criada com sucesso!!")
            self.modal.destroy()
            
            
            
            
        else:
            messagebox.showinfo("Ganhos" , "Algo deu Errado no cadastro!!")

    def DeleteEntrada(self):
        modal = tkk.Toplevel()
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