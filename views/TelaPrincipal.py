import tkinter as tk
from tkinter import messagebox
import customtkinter
class TelaPrincipal:
    def __init__(self,root) -> None:
        # criando janela
        self.janela = root
        self.janela.title("Minha Interface Tkinter")
        self.janela.geometry("300x200")



        self.createMenu()
        self.createMain()

    def createMain(self):
       pass
    def createMenu(self):
        self.menu_bar = tk.Menu(self.janela)

        self.entradaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Entrada", menu=self.entradaMenu)
        self.entradaMenu.add_command(label="Cadastrar" ,command=print('oi'))
        self.entradaMenu.add_separator()
        self.entradaMenu.add_command(label="Editar" ,command=print('oi'))
        self.entradaMenu.add_separator()
        self.entradaMenu.add_command(label="Excluir" ,command=print('oi'))
        
        
        self.saidaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Gastos", menu=self.saidaMenu)
        self.saidaMenu.add_command(label="Cadastrar" ,command=print('oi'))
        self.saidaMenu.add_separator()
        self.saidaMenu.add_command(label="Editar" ,command=print('oi'))
        self.saidaMenu.add_separator()
        self.saidaMenu.add_command(label="Excluir" ,command=print('oi'))

        self.financaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Investimentos", menu=self.financaMenu)
        self.financaMenu.add_command(label="Cadastrar" ,command=print('oi'))
        self.financaMenu.add_separator()
        self.financaMenu.add_command(label="Editar" ,command=print('oi'))
        self.financaMenu.add_separator()
        self.financaMenu.add_command(label="Excluir" ,command=print('oi'))

        self.janela.config(menu=self.menu_bar)
if __name__ == '__main__':
    root = customtkinter.CTk()
    app = TelaPrincipal(root)
    root.mainloop()