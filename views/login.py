import TelaPrincipal as Tp
import tkinter as tk
from tkinter import messagebox
import customtkinter

class MinhaInterface:
    def __init__(self, root):
        # criando janela
        self.janela = root
        self.janela.title("Login")
        largura = 800
        altura = 600
        x_offset = 100  
        y_offset = 50  
        # self.janela.geometry("400x440")
        self.janela.geometry(f"{largura}x{altura}+{x_offset}+{y_offset}")
        
        self.createLogin()

    def createLogin(self):
        # Criar um rótulo
        self.frameLogin = customtkinter.CTkFrame(master = self.janela, width=100, height=100)
        self.frameLogin.pack(padx=120, pady=120, fill=tk.BOTH, expand=True)

        self.labelUser = customtkinter.CTkLabel(self.frameLogin, text="Digite seu User!",fg_color="transparent")
        self.entryUser = customtkinter.CTkEntry(self.frameLogin, placeholder_text="Usuario")

        self.labelPass = customtkinter.CTkLabel(self.frameLogin, text="Digite sua Senha!",fg_color="transparent")
        self.entryPass = customtkinter.CTkEntry(self.frameLogin, placeholder_text="Senha")
        
        self.textLabel = tk.Text(self.frameLogin, padx=10, pady=50)
        self.labelUser.pack(pady=(75,3))
        self.entryUser.pack(pady=1)
        self.labelPass.pack(pady=3)
        self.entryPass.pack(pady=1)
        # Criar um botão
        self.buttonLogin = customtkinter.CTkButton(self.frameLogin, text="Login", command=self.loginButton)
        self.buttonRegister = customtkinter.CTkButton(self.frameLogin, text="Cadastrar", command=self.RegisterButton)

        self.buttonLogin.pack(pady=5,padx=20,anchor="center")
        
        self.buttonRegister.pack(pady=5,padx=20,anchor="center")


        
    def RegisterButton(self):
        modal = tk.Toplevel()
        modal.title("Registro de Usuário")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient(parent)
        modal.grab_set()

        # Adiciona widgets ao modal
        label = tk.Label(modal, text="Este é um modal.")
        label.pack(pady=10)

        close_button = tk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

        return modal
        
    
    def loginButton(self):
        pass

if __name__ == '__main__':
    root = customtkinter.CTk()
    app = MinhaInterface(root)
    root.mainloop()
    