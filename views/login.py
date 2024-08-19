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
import json

#Extends Files
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../controllers'))
sys.path.append(module_path)
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../views'))
sys.path.append(module_path)
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils'))
sys.path.append(module_path)
import controllerUser
import TelaPrincipal





class MinhaInterface:
    def __init__(self, root):
        # criando janela
        self.janela = root
        self.janela.title("Login")
        largura = 800
        altura = 600
        x_offset = 100  
        y_offset = 50  
        
        self.janela.geometry(f"{largura}x{altura}+{x_offset}+{y_offset}")

        with open('./utils/dicionario.json','r',encoding='utf-8') as file:
            self.dicionario = json.load(file)

        self.linguaAtual = self.dicionario['language']['pt-br']['LoginScreen']    
        self.linguaAtualRegistro = self.dicionario['language']['pt-br']['registrationScreen']    

    def foc_in(self, *args):
        self.delete('0', 'end')
        
    def createLogin(self):
        # Criar um rótulo
        
        self.frameLogin = tkk.Labelframe(master = self.janela, width=100, height=100 , bootstyle="dark", text="Login")
        self.frameLogin.pack(padx=120, pady=120, fill=tk.BOTH, expand=True)
    
        self.menuBarLingua = tkk.Frame(self.frameLogin)
        self.menuBarLingua.pack(fill=X)

        menuButtonLingua = tkk.Menubutton(self.menuBarLingua,text=f'🌎 {self.linguaAtual['language']}',bootstyle='outline')
        menuButtonLingua.pack(pady= 1,padx=10,side=RIGHT)

        menu2 = tkk.Menu(menuButtonLingua, tearoff=0)
        
        menuButtonLingua.config(menu=menu2)

        menu2.add_command(label="PT-BR", command=lambda:self.choosePortuguesse())
        menu2.add_command(label="EN", command= lambda:self.chooseEnglish())
        menu2.add_command(label="ES", command= self.chooseSpanish)

        

        loginUserVar = tkk.StringVar()
      
        self.labelUser = tkk.Label(self.frameLogin, text=f"👤 {self.linguaAtual['user']}")
        self.entryUser = tkk.Entry(self.frameLogin,textvariable=loginUserVar)
        ToolTip(self.entryUser,text = 'Insira seu Usuário')        

        loginPassVar = tkk.StringVar()
        self.labelPass = tkk.Label(self.frameLogin, text=f"🔑 {self.linguaAtual['passWord']}")
        self.entryPass = tkk.Entry(self.frameLogin,textvariable=loginPassVar , show='*')
        ToolTip(self.entryPass,text = 'Insira sua senha')     
        
        
        self.textLabel = tkk.Text(self.frameLogin, padx=10, pady=50)
        self.labelUser.pack(pady=(55,3))
        self.entryUser.pack(pady=1)
        self.labelPass.pack(pady=3)
        self.entryPass.pack(pady=1)
        # Criar um botão
        self.buttonLogin = tkk.Button(self.frameLogin, text=   f"   {self.linguaAtual['login']}   ", command=lambda : self.loginButton({"nome":loginUserVar.get(),"senha":loginPassVar.get(),"email":"","id":""}))
        self.buttonRegister = tkk.Button(self.frameLogin, text=f" {self.linguaAtual['register']}", command=self.RegisterButton)

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
            messagebox.showinfo("Cadastro" , f"{self.linguaAtualRegistro['successMessage']['successRegistration']}")
            modal.destroy()
        else:
            messagebox.showinfo("Cadastro" , f"{self.linguaAtualRegistro['ErrorMessage']['errorRegistration']}")

        
        
    def validation(self,params,senhaConfirm):

        if(params['senha'] != senhaConfirm):
            return ["SE",f"{self.linguaAtualRegistro['ErrorMessage']['differentPasswords']}"]
        elif( params['senha'] == "" or 
              params['email'] == "" or
              params['nome'] == "" or
              senhaConfirm == ""
            ):
            return ["CZ",f"{self.linguaAtualRegistro['ErrorMessage']['blankFields']}"]
        elif("@" not in params['email']):
            return ["EI",f"{self.linguaAtualRegistro['ErrorMessage']['invalidEmail']}"]

        return "OK"


    def loginButton(self,params):
        
        LoginOk = controllerUser.User(params).loginUser()
        if(LoginOk[0] == 'OK'):
            messagebox.showinfo("Usuario" ,f'{self.linguaAtual['successMessage']['loginsuccess']}')
            userAtual = LoginOk[1]
            
            self.frameLogin.destroy()

            
            TelaPrincipal.TelaPrincipal(self.janela,userAtual)

        else:
            messagebox.showinfo("Usuario" ,f'{self.linguaAtual['ErrorMessage']['loginerror']}')
    def choosePortuguesse(self):
        self.linguaAtual = self.dicionario['language']['pt-br']['LoginScreen'] 
        self.linguaAtualRegistro = self.dicionario['language']['pt-br']['registrationScreen']   
        self.resetLoginScreen()
        
        
    def chooseEnglish(self):
        self.linguaAtual = self.dicionario['language']['en']['LoginScreen']   
        self.linguaAtualRegistro = self.dicionario['language']['en']['registrationScreen']  
        self.resetLoginScreen()
    def chooseSpanish(self):
        
        self.linguaAtual = self.dicionario['language']['es']['LoginScreen']  
        self.linguaAtualRegistro = self.dicionario['language']['es']['registrationScreen']   
        self.resetLoginScreen()

    def resetLoginScreen(self):

        self.frameLogin.destroy()
        self.createLogin()


    def RegisterButton(self):
        modal = tkk.Toplevel()
        modal.title("Registro de Usuário")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        # Adiciona widgets ao modal
        userName = tkk.StringVar()        
        self.labelUser = tkk.Label(modal, text=f"👤{self.linguaAtualRegistro['user']}")
        self.entryUser = tkk.Entry(modal, textvariable=userName)
        ToolTip(self.entryUser,text = f'{self.linguaAtualRegistro['desiredUserName']}')     
        self.labelUser.pack(pady=(5))
        self.entryUser.pack(pady=(5))

        userEmail = tkk.StringVar()
        self.labelEmail = tkk.Label(modal,text=f"📧{self.linguaAtualRegistro['email']}")
        self.entryEmail = tkk.Entry(modal, textvariable=userEmail)
        ToolTip(self.entryEmail,text = f'{self.linguaAtualRegistro['enterEmail']}')     
        self.labelEmail.pack(pady=(5))
        self.entryEmail.pack(pady=(5))

        userPassCadastro = tkk.StringVar()
        self.labelPassCadastro = tkk.Label(modal, text=f"🔑{self.linguaAtualRegistro['passWord']}")
        self.entryPassCadastro = tkk.Entry(modal,show='*', textvariable=userPassCadastro)
        ToolTip(self.entryPassCadastro,text = f'{self.linguaAtualRegistro['enterPassword']}')     
        self.labelPassCadastro.pack(pady=(5))
        self.entryPassCadastro.pack(pady=(5))
        
        userPassConfirm = tkk.StringVar()
        self.labelPassConfirm = tkk.Label(modal, text=f"🔑{self.linguaAtualRegistro['passWordConfirm']}")
        self.entryPassConfirm = tkk.Entry(modal,show='*', textvariable=userPassConfirm)
        ToolTip(self.entryPassConfirm,text = f'{self.linguaAtualRegistro['enterPasswordAgain']}')  
        self.labelPassConfirm.pack(pady=(5))
        self.entryPassConfirm.pack(pady=(5))

        self.check_var = tkk.StringVar(value="on")
        self.checkbox = tkk.Checkbutton(modal, text=f"{self.linguaAtualRegistro['termsOfUse']}",
                                     variable=self.check_var, onvalue="on", offvalue="off")
        
        self.checkbox.pack(pady=5)
        userCreatedOk = ''

        self.buttonRegister = tkk.Button(modal, text=f"💾 {self.linguaAtualRegistro['register']}", command=lambda : self.register({"nome": userName.get(),"email": userEmail.get(),"senha": userPassCadastro.get(),"id":""},modal,userPassConfirm.get()))
        
      
        

        self.buttonRegister.pack(pady=(5))
        if userCreatedOk != '':
            messagebox.showinfo("Alerta", "Este é um alerta!")

        
        close_button = tkk.Button(modal, text=f"❌ {self.linguaAtualRegistro['close']}", command=modal.destroy)
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
    
