import tkinter as tk
from tkinter import messagebox
import customtkinter
import os
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

        labelTitle = customtkinter.CTkLabel(self.janela, text="Inserção de Entrada ou Lucros", fg_color="transparent",font=("",23))
        labelTitle.pack(pady=5)


        labelOpcaoEntrada = customtkinter.CTkLabel(self.janela, text="Tipo de Entrada:", fg_color="transparent")
        labelOpcaoEntrada.pack(pady=2)

        self.optionmenu_var = customtkinter.StringVar()
        optionmenu = customtkinter.CTkOptionMenu(self.janela,values=["Salario", "Aluguel","Outros"],
                                         variable=self.optionmenu_var
                                         )
        optionmenu.pack(pady=5)

        
        labelOpcaoValor = customtkinter.CTkLabel(self.janela, text="Valor da Entrada:", fg_color="transparent")
        labelOpcaoValor.pack(pady=2)

        self.valueSlider = customtkinter.IntVar()
        slider = customtkinter.CTkSlider(self.janela, from_=0, to=50000, variable=self.valueSlider, command = self.catchValue)

        slider.pack(pady=5)
        

        self.entryValue = customtkinter.CTkEntry(self.janela, placeholder_text=0)

        self.entryValue.pack(pady=5)

        add_button = customtkinter.CTkButton(self.janela, text="Inserir" ,command=lambda:self.insertEntrace({"nome_entrada":self.optionmenu_var.get(),"valor":self.valueSlider.get(),"id_user":self.userAtual[0][0],"id_entries":"0"}))
        add_button.pack(pady=5)
        # Desabilita interação com a janela principal
    
        close_button = customtkinter.CTkButton(self.janela, text="Fechar", command= self.leaveCadastro)

        close_button.pack(pady=5)
    def leaveCadastro(self):
        self.janela.destroy()
        root = customtkinter.CTk()
        TP.TelaPrincipal(root,self.userAtual)
        root.mainloop()

    def EditEntrada(self):
        modal = tk.Toplevel()
        modal.title("Edição de Entrada/Lucro")
        modal.geometry("800x600")
        
        tabview = customtkinter.CTkTabview(master=modal)
        tabview.pack(padx=20, pady=20)

        tabview.add("tab 1")  # add tab at the end
        tabview.add("tab 2")  # add tab at the end
        tabview.set("tab 2")
        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

    def insertEntrace(self,params):
        cadastroEntradaOK = controllerEntries.Entrie(params).createEntries()
        if(cadastroEntradaOK=="OK"):
            messagebox.showinfo("Ganhos" , "Entrada de ganhos criada com sucesso!!")
            self.janela.destroy()
            root = customtkinter.CTk()
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
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
        
    def catchValue(self,value):
        self.entryValue.delete(0, customtkinter.END)  # Primeiro, limpa o conteúdo atual
        self.entryValue.insert(0,str(self.valueSlider.get() )) 

if __name__ == '__main__':
    root = customtkinter.CTk()
    user = ''
    app = Entrada(root,user)
    root.mainloop()