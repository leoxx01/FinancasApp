import TelaPrincipal as Tp
import tkinter as tk
from tkinter import messagebox
import customtkinter

class MinhaInterface:
    def __init__(self, root):
        # criando janela
        self.janela = root
        self.janela.title("Login")
        self.janela.geometry("400x440")
        
        self.createLogin()

    def createLogin(self):
        # Criar um rótulo
        self.labelUser = customtkinter.CTkLabel(self.janela, text="Digite seu User!",fg_color="transparent")
        self.entryUser = customtkinter.CTkEntry(self.janela, placeholder_text="Usuario")
        self.labelPass = customtkinter.CTkLabel(self.janela, text="Digite sua Senha!",fg_color="transparent")
        self.entryPass = customtkinter.CTkEntry(self.janela, placeholder_text="Senha")
        
        self.textLabel = tk.Text(self.janela, padx=10, pady=50)
        self.labelUser.pack(pady=3)
        self.entryUser.pack(pady=1)
        self.labelPass.pack(pady=3)
        self.entryPass.pack(pady=1)
        # Criar um botão
        self.buttonLogin = customtkinter.CTkButton(self.janela, text="Login", command=self.clickButton,anchor='center')
        self.buttonRegister = customtkinter.CTkButton(self.janela, text="Cadastrar", command=self.clickButton)

        self.buttonLogin.pack(pady=5,padx=20,anchor="center")
        
        self.buttonRegister.pack(pady=5,padx=20,anchor="center")

    def clickButton(self):
        messagebox.showinfo("Cadastro", "Cadastro Feito com sucesso!")

if __name__ == '__main__':
    root = customtkinter.CTk()
    app = MinhaInterface(root)
    root.mainloop()
    