import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class teste():
    def __init__(self,janela) -> None:
        self.janela = janela
# Função de inicialização da janela principal
    def init_main_window(self):
            # Criação da janela principal com um tema específico
            
            self.janela.title("Exemplo de OptionMenu com ttkbootstrap")
            self.janela.geometry("300x200")

            # Criação da variável associada ao OptionMenu
            

            # Lista de opções para o OptionMenu
            opcoes = ["Salario","Salario", "Aluguel", "Outros"]
            self.optionmenu_var = ttk.StringVar()
            # Criação do OptionMenu estilizado
            optionmenu = ttk.OptionMenu(
                self.janela,
                self.optionmenu_var,
                *opcoes,
                bootstyle="primary"
            )

            # Adiciona o OptionMenu ao layout da janela
            optionmenu.pack(pady=20)

            # Inicia o loop principal da interface gráfica
            self.janela.mainloop()

# Inicializa a janela principal
if __name__ == "__main__":
    
    janela = ttk.Window()
    teste(janela).init_main_window()
