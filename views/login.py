import TelaPrincipal as Tp
import json
import tkinter as tk
import sys
import os
from tkinter import messagebox
import customtkinter
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../controllers'))
sys.path.append(module_path)
import controllerUser

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
        modal.transient()
        modal.grab_set()
        
       
        
        
        # Adiciona widgets ao modal
        userName = customtkinter.StringVar()        
        self.labelUser = customtkinter.CTkLabel(modal, text="Digite seu Usuário!",fg_color="transparent")
        self.entryUser = customtkinter.CTkEntry(modal, textvariable=userName,placeholder_text="Usuario")
        self.labelUser.pack(pady=(5))
        self.entryUser.pack(pady=(5))

        userEmail = customtkinter.StringVar()
        self.labelEmail = customtkinter.CTkLabel(modal,text="Digite seu Email!",fg_color="transparent")
        self.entryEmail = customtkinter.CTkEntry(modal, textvariable=userEmail ,placeholder_text="Email")
        self.labelEmail.pack(pady=(5))
        self.entryEmail.pack(pady=(5))

        userPass = customtkinter.StringVar()
        self.labelPass = customtkinter.CTkLabel(modal, text="Digite sua Senha!",fg_color="transparent")
        self.entryPass = customtkinter.CTkEntry(modal, textvariable=userPass,placeholder_text="Senha")
        self.labelPass.pack(pady=(5))
        self.entryPass.pack(pady=(5))
        
        userPassConfirm = customtkinter.StringVar()
        self.labelPassConfirm = customtkinter.CTkLabel(modal, text="Digite Novamente sua Senha!",fg_color="transparent")
        self.entryPassConfirm = customtkinter.CTkEntry(modal, textvariable=userPassConfirm, placeholder_text="Senha")
        self.labelPassConfirm.pack(pady=(5))
        self.entryPassConfirm.pack(pady=(5))

        self.check_var = customtkinter.StringVar(value="on")
        self.checkbox = customtkinter.CTkCheckBox(modal, text="Li e estou de acordo com os termos de uso!!",
                                     variable=self.check_var, onvalue="on", offvalue="off")
        
        self.checkbox.pack(pady=5)
        userCreatedOk = ''
        self.buttonRegister = customtkinter.CTkButton(modal, text="Cadastrar", command=lambda :controllerUser.User({"nome": userName.get(),"email": userEmail.get(),"senha": userPass.get(),"id":""}).createUser())
        self.buttonRegister.pack(pady=(5))
        if userCreatedOk != '':
            messagebox.showinfo("Alerta", "Este é um alerta!")

        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

        

        return modal
        
    
    def loginButton(self):
        pass

if __name__ == '__main__':
    root = customtkinter.CTk()
    app = MinhaInterface(root)
    root.mainloop()
    