import customtkinter
import tkinter as tk
from tkinter import messagebox

class TelaPrincipal:
    def __init__(self, root) -> None:
        # criando janela
        self.janela = root
        self.janela.title("Minha Interface Tkinter")
        self.janela.geometry("300x200")

        self.createMain()

    def createMain(self):
        self.label = tk.Label(self.janela, text="aaahhh", padx=10)
    

if __name__ == '__main__':
    root = tk.Tk()
    app = TelaPrincipal(root)
    root.mainloop()