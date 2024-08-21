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
import controllerTypeEntries
from ttkbootstrap.widgets import DateEntry
from ttkbootstrap.constants import *

class TypeEntrieView():

    def __init__(self,root) -> None:
        
        self.janela = root
        

    def screenAddTypeEntrie(self):

        self.modal =  tkk.Toplevel()
        self.modal.geometry("800x600")

        labelTitle = tkk.Label(self.modal, text="Inserção de Tipos de Receita",font=("",23))
        labelTitle.pack(pady=5)

        tkk.Separator(bootstyle="info",master=self.modal).pack(fill=X,padx=100,pady=2)

        labelNameEntrie = tkk.Label(self.modal,text="Tipo de Receita")
        labelNameEntrie.pack(pady=5)

        self.entryNameEntrieVar = tkk.StringVar()
        entryNameEntrie = tkk.Entry(self.modal,textvariable=self.entryNameEntrieVar)
        entryNameEntrie.pack(pady=5)

        buttonSubmit = tkk.Button(self.modal,text="Cadastrar",bootstyle="success",command=self.addTypeEntrie)
        buttonSubmit.pack(pady=2)
        buttonCancel = tkk.Button(self.modal,text="Fechar",bootstyle="danger")
        buttonCancel.pack()

        self.modal.transient()
        self.modal.grab_set()
        
    def addTypeEntrie(self):
        addType = controllerTypeEntries.TypeEntriesController({"nameEntrie":self.entryNameEntrieVar.get()}).createTypeEntries()
        if(addType == "OK"):
            messagebox.showinfo("Tipo Receita" , "Tipo de receita criado com sucesso!!")
            self.modal.destroy()  
        else:  
            messagebox.showinfo("Tipo Receita" , "Algo deu errado!!")

if __name__ == '__main__':
    root = tkk.Window()
    
    app = TypeEntrieView(root)
    root.mainloop()