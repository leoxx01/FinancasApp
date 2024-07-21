import TelaPrincipal as Tp
import tkinter as tk
from tkinter import messagebox

class MinhaInterface:
    def __init__(self, root):
        # criando janela
        self.janela = root
        self.janela.title("Login")
        self.janela.geometry("400x440")

        self.createLogin()

    def createLogin(self):
        # Criar um rótulo
        self.label = tk.Label(self.janela, text="Está funcionando!")
        self.textLabel = tk.Text(self.janela, padx=10, pady=50)
        self.label.pack(pady=10)

        # Criar um botão
        self.button = tk.Button(self.janela, text="Clique-me", command=self.clickButton)
        self.button.pack(pady=15)

    def clickButton(self):
        messagebox.showinfo("Cadastro", "Cadastro Feito com sucesso!")

if __name__ == '__main__':
    root = tk.Tk()
    app = MinhaInterface(root)
    root.mainloop()