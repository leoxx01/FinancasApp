import TelaPrincipal as Tp
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
import ttkbootstrap as tkk
from ttkbootstrap.constants import *
import sys
import os
from tkinter import messagebox
from ttkbootstrap.tooltip import ToolTip
import TelaPrincipal
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../controllers'))
sys.path.append(module_path)
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../views'))
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

    def foc_in(self, *args):
        self.delete('0', 'end')
        
    def createLogin(self):
        # Criar um rótulo
        
        
        self.frameLogin = tkk.Labelframe(master = self.janela, width=100, height=100 , bootstyle="dark", text="Login")
        self.frameLogin.pack(padx=120, pady=120, fill=tk.BOTH, expand=True)

        loginUserVar = tkk.StringVar()
        
        

        self.labelUser = tkk.Label(self.frameLogin, text="👤 Usuario")
        self.entryUser = tkk.Entry(self.frameLogin,textvariable=loginUserVar)
        ToolTip(self.entryUser,text = 'Insira seu Usuário')        

        loginPassVar = tkk.StringVar()
        self.labelPass = tkk.Label(self.frameLogin, text="🔑 Senha")
        self.entryPass = tkk.Entry(self.frameLogin,textvariable=loginPassVar , show='*')
        ToolTip(self.entryPass,text = 'Insira sua senha')     
        
        
        self.textLabel = tkk.Text(self.frameLogin, padx=10, pady=50)
        self.labelUser.pack(pady=(75,3))
        self.entryUser.pack(pady=1)
        self.labelPass.pack(pady=3)
        self.entryPass.pack(pady=1)
        # Criar um botão
        self.buttonLogin = tkk.Button(self.frameLogin, text=   "   Login   ", command=lambda : self.loginButton({"nome":loginUserVar.get(),"senha":loginPassVar.get(),"email":"","id":""}))
        self.buttonRegister = tkk.Button(self.frameLogin, text="Cadastrar", command=self.RegisterButton)

        self.buttonLogin.pack(pady=5,padx=20,anchor="center")
        
        self.buttonRegister.pack(pady=5,padx=20,anchor="center")
    
    def register(self,params,modal,senhaConfirm):
        registerOk = "NOKSE"

        valitationAll = self.validation(params,senhaConfirm)
        if(valitationAll == "OK"):
            registerOk = controllerUser.User(params).createUser()
           
        else:
            messagebox.showinfo("Cadastro" , valitationAll[1])


        if(registerOk == 'OK'):
            messagebox.showinfo("Cadastro" , "Criado com sucesso!!")
            modal.destroy()
        else:
            print('o')
            messagebox.showinfo("Cadastro" , "Email já cadastrado")

        
        
    def validation(self,params,senhaConfirm):

        if(params['senha'] != senhaConfirm):
            return ["SE","Senha estão divergente"]
        elif( params['senha'] == "" or 
              params['email'] == "" or
              params['nome'] == "" or
              senhaConfirm == ""
            ):
            return ["CZ","Verifique os Campos preenchidos"]
        elif("@" not in params['email']):
            return ["EI","Email Invalido"]

        return "OK"

    def on_closing(self):
        self.janela.destroy()

    def loginButton(self,params):
        
        LoginOk = controllerUser.User(params).loginUser()
        if(LoginOk[0] == 'OK'):
            messagebox.showinfo("Usuario" , "Login efetuado com sucesso!!!")
            userAtual = LoginOk[1]
            
            self.janela.protocol("WM_DELETE_WINDOW", self.on_closing)
            
            TelaPrincipal.TelaPrincipal(self.janela,userAtual)

        else:
            messagebox.showinfo("Usuario" , "Erro ao etuar o login!!!")
      
        

    def RegisterButton(self):
        modal = tkk.Toplevel()
        modal.title("Registro de Usuário")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        # Adiciona widgets ao modal
        userName = tkk.StringVar()        
        self.labelUser = tkk.Label(modal, text="👤Usuário")
        self.entryUser = tkk.Entry(modal, textvariable=userName)
        ToolTip(self.entryUser,text = 'Insira o nome de usuário desejado')     
        self.labelUser.pack(pady=(5))
        self.entryUser.pack(pady=(5))

        userEmail = tkk.StringVar()
        self.labelEmail = tkk.Label(modal,text="📧Email")
        self.entryEmail = tkk.Entry(modal, textvariable=userEmail)
        ToolTip(self.entryEmail,text = 'Insira seu email')     
        self.labelEmail.pack(pady=(5))
        self.entryEmail.pack(pady=(5))

        userPassCadastro = tkk.StringVar()
        self.labelPassCadastro = tkk.Label(modal, text="🔑Senha")
        self.entryPassCadastro = tkk.Entry(modal,show='*', textvariable=userPassCadastro)
        ToolTip(self.entryPassCadastro,text = 'Insira sua senha')     
        self.labelPassCadastro.pack(pady=(5))
        self.entryPassCadastro.pack(pady=(5))
        
        userPassConfirm = tkk.StringVar()
        self.labelPassConfirm = tkk.Label(modal, text="🔑Cofirme a Senha")
        self.entryPassConfirm = tkk.Entry(modal,show='*', textvariable=userPassConfirm)
        ToolTip(self.entryPassConfirm,text = 'Insira sua senha novamente')  
        self.labelPassConfirm.pack(pady=(5))
        self.entryPassConfirm.pack(pady=(5))

        self.check_var = tkk.StringVar(value="on")
        self.checkbox = tkk.Checkbutton(modal, text="Li e estou de acordo com os termos de uso!!",
                                     variable=self.check_var, onvalue="on", offvalue="off")
        
        self.checkbox.pack(pady=5)
        userCreatedOk = ''

        self.buttonRegister = tkk.Button(modal, text="💾 Cadastrar", command=lambda : self.register({"nome": userName.get(),"email": userEmail.get(),"senha": userPassCadastro.get(),"id":""},modal,userPassConfirm.get()))
        
      
        

        self.buttonRegister.pack(pady=(5))
        if userCreatedOk != '':
            messagebox.showinfo("Alerta", "Este é um alerta!")

        
        close_button = tkk.Button(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

        

        return modal
  
def show_tooltip(event, tooltip):
    tooltip.place(x=event.x_root - event.widget.winfo_rootx(), y=event.y_root - event.widget.winfo_rooty())

def hide_tooltip(tooltip):
    tooltip.place_forget()

if __name__ == '__main__':
    root = tkk.Window()
    app = MinhaInterface(root)
    loginWindown = root.mainloop()
    
