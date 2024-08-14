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

class Entrada:
    def __init__(self,root,user,tree) -> None:

        self.janela = root
        self.tree = tree
        self.userAtual = user
        self.cadastroEntradaFinsh = ""
        
        
    def cadastroEntrada(self):
        self.modal = tkk.Toplevel()
        self.modal.title("Inserção de Entrada/Lucro")
        
        self.modal.geometry("800x600")

        labelTitle = tkk.Label(self.modal, text="Inserção de Entrada ou Lucros",font=("",23))
        labelTitle.pack(pady=5)
        tkk.Separator(bootstyle="info",master=self.modal).pack(fill=X,padx=100,pady=2)

        labelOpcaoEntrada = tkk.Label(self.modal, text="Tipo de Entrada:")
        labelOpcaoEntrada.pack(pady=2)

        opcaoesNew = controllerTypeEntries.TypeEntriesController({"nameEntrie":""}).selectAllTypeEntries()

        print(opcaoesNew[0][0])
        opcaoes = []
        for i in opcaoesNew:
            opcaoes.append(i[0])
        
        self.optionmenu_var = tkk.StringVar()
        
        optionmenu = tkk.OptionMenu(
                                    self.modal,
                                    self.optionmenu_var,
                                    *opcaoes,
                                    bootstyle="primary",
                                    direction="flush"
                                    
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
        

        add_button = tkk.Button(self.modal, text="Inserir",bootstyle="success" ,command=lambda:self.insertEntrace({"nome_entrada":self.optionmenu_var.get(),"valor":self.entryValue.get(),"id_user":self.userAtual,"id_entries":"0"}))
        add_button.pack(pady=5)
        # Desabilita interação com a janela principal
    
        close_button = tkk.Button(self.modal, text="Fechar",bootstyle="danger", command= self.modal.destroy)

        close_button.pack(pady=5)
        
        
 
            

    def EditEntrada(self,item_values):
        self.modal = tkk.Toplevel()
        self.modal.title("Edição de Entrada/Lucro")
        self.modal.geometry("800x600")

        labelTitle = tkk.Label(self.modal, text="Edição | Exclusão de Receita",font=("",23))
        labelTitle.pack(pady=5)
        tkk.Separator(bootstyle="info",master=self.modal).pack(fill=X,padx=100,pady=2)

             
        

        # Desabilita interação com a janela principal
        self.modal.transient()
        self.modal.grab_set()
        
        labelReceita = tkk.Label(self.modal,text="Tipo de Receita").pack()
        self.tipoReceita = tkk.Entry(self.modal)
        self.tipoReceita.pack()

        self.valorEdit = tkk.IntVar()
        labelValor = tkk.Label(self.modal,text="Valor").pack()
        self.valorReceita = tkk.Entry(self.modal,textvariable=self.valorEdit)
        self.valorReceita.pack()
        
        self.tipoReceita.delete(0, tkk.END)  
        self.tipoReceita.insert(0,str(item_values[1])) 
        self.valorReceita.delete(0, tkk.END)  
        self.valorReceita.insert(0,str(item_values[2])) 

        self.tipoReceita.configure(state="readonly")

        # self.tipoReceita.configure(state="disabled")

        editButton = tkk.Button(self.modal,text="Atualizar",bootstyle="info-outline",command=lambda:self.editItem(item_values)).pack(pady=5)

        deleteButton = tkk.Button(self.modal,text="Deletar",bootstyle="danger-outline",command= lambda:self.deleteItem({
            'id': item_values[0],
            'nome_entrada': "",
            'valor': "",
            'id_user': ""
        })).pack(pady=5)
       
    def editItem(self,values):
        print(values,self.userAtual)
        updateItem = controllerEntries.Entrie({
            'id': values[0],
            'nome_entrada': values[1],
            'valor': str(self.valorEdit.get()),
            'id_user': self.userAtual
        }).updateEntries()

        if(updateItem == "OK"):
            self.modal.destroy()
            self.popularTree()

    def deleteItem(self,params):
        deleteItemOk = controllerEntries.Entrie(params).deleteEntries()
        
        if(deleteItemOk == "OK"):
            self.modal.destroy()
            self.popularTree()
           

    def insertEntrace(self,params):
        cadastroEntradaOK = controllerEntries.Entrie(params).createEntries()
        
        if(cadastroEntradaOK=="OK"):
            self.cadastroEntradaFinsh = "OK"
            messagebox.showinfo("Ganhos" , "Entrada de ganhos criada com sucesso!!")
            self.modal.destroy()
        
            self.popularTree()
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

    def popularTree(self):
        
        for item in self.tree.get_children():
                self.tree.delete(item)

        data2  = controllerEntries.Entrie({"nome_entrada":"","valor":"","id_user":str(self.userAtual),"id_entries":""}).getItemById()

        for dado in data2[1]:
            self.tree.insert("", "end", values=(dado[0],dado[1],dado[2]))

if __name__ == '__main__':
    root = tkk.Window()
    user = ''
    app = Entrada(root,user)
    root.mainloop()