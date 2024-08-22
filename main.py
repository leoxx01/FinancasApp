
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
import ttkbootstrap as tkk
from ttkbootstrap.constants import *
import sys
import os
from tkinter import messagebox
from ttkbootstrap.tooltip import ToolTip
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './views'))
sys.path.append(module_path)
import login

class MainApp:
    def __init__(self,root) -> None: 
        login.MinhaInterface(root).createLogin()
        
if __name__ == '__main__':
    root = tkk.Window()
    app = MainApp(root)
    loginWindown = root.mainloop()
