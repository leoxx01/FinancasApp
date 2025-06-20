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
import controllerEntries
import controllerTypeEntries
import TelaPrincipal as TP

class Investimento:
    def __init__(self,root,user,tree) -> None:

        self.janela = root
        self.tree = tree
        self.userAtual = user
        self.cadastroInvestimentosFinsh = ""
        

if __name__ == '__main__':
    root = tkk.Window()
    user = ''
    app = Investimento(root,user)
    root.mainloop()