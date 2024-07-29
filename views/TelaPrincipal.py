import tkinter as tk
from tkinter import messagebox
import customtkinter
class TelaPrincipal:
    def __init__(self,root) -> None:
        # criando janela
        self.janela = root
        self.janela.title("Gerenciador de finanças")
        self.janela.geometry("300x200")



        self.createMenu()
        self.createMain()

    def createMain(self):
       pass
    def createMenu(self):
        self.menu_bar = tk.Menu(self.janela)

        self.entradaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Entrada", menu=self.entradaMenu)
        self.entradaMenu.add_command(label="Cadastrar" ,command=self.cadastroEntrada)
        self.entradaMenu.add_separator()
        self.entradaMenu.add_command(label="Editar" ,command=self.EditEntrada)
        self.entradaMenu.add_separator()
        self.entradaMenu.add_command(label="Excluir" ,command=self.DeleteEntrada)
        
        
        self.saidaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Gastos", menu=self.saidaMenu)
        self.saidaMenu.add_command(label="Cadastrar" ,command=self.cadastroSaida)
        self.saidaMenu.add_separator()
        self.saidaMenu.add_command(label="Editar" ,command=self.editSaida)
        self.saidaMenu.add_separator()
        self.saidaMenu.add_command(label="Excluir" ,command=self.deleteSaida)

        self.financaMenu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Investimentos", menu=self.financaMenu)
        self.financaMenu.add_command(label="Cadastrar" ,command=self.cadastroInvestimentos)
        self.financaMenu.add_separator()
        self.financaMenu.add_command(label="Editar" ,command=self.editInvestimentos)
        self.financaMenu.add_separator()
        self.financaMenu.add_command(label="Excluir" ,command=self.deleteInvestimentos)

        self.janela.config(menu=self.menu_bar)

    def cadastroEntrada(self):
        modal = tk.Toplevel()
        modal.title("Inserção de Entrada/Lucro")
        modal.geometry("800x600")

        labelTitle = customtkinter.CTkLabel(modal, text="Inserção de Entrada ou Lucros", fg_color="transparent",font=("",23))
        labelTitle.pack(pady=5)


        labelOpcaoEntrada = customtkinter.CTkLabel(modal, text="Tipo de Entrada:", fg_color="transparent")
        labelOpcaoEntrada.pack(pady=2)

        optionmenu_var = customtkinter.StringVar()
        optionmenu = customtkinter.CTkOptionMenu(modal,values=["Salario", "Aluguel","Outros"],
                                         variable=optionmenu_var)
        optionmenu.pack(pady=5)

        
        labelOpcaoValor = customtkinter.CTkLabel(modal, text="Valor da Entrada:", fg_color="transparent")
        labelOpcaoValor.pack(pady=2)

        valueSlider = customtkinter.IntVar()
        slider = customtkinter.CTkSlider(modal, from_=0, to=50000, variable=valueSlider)

        slider.pack(pady=5)
        
        entry = customtkinter.CTkEntry(modal, placeholder_text=valueSlider,state="disabled")

        entry.pack(pady=5)

        add_button = customtkinter.CTkButton(modal, text="Inserir" )
        add_button.pack(pady=5)
        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        

        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy )
        close_button.pack(pady=5)

    def EditEntrada(self):
        modal = tk.Toplevel()
        modal.title("Edição de Entrada/Lucro")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

    def DeleteEntrada(self):
        modal = tk.Toplevel()
        modal.title("Exclusão de Entrada/Lucro")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
    
    
    def cadastroSaida(self):
        modal = tk.Toplevel()
        modal.title("Inserção de Saida/Gastos")
        modal.geometry("800x600")

        labelTitle = customtkinter.CTkLabel(modal, text="Inserção de Saida/Gastos", fg_color="transparent",font=("",23))
        labelTitle.pack(pady=5)

        labelOpcaoSaida = customtkinter.CTkLabel(modal, text="Tipo de Gastos:", fg_color="transparent")
        labelOpcaoSaida.pack(pady=2)

        entrySaida = customtkinter.CTkEntry(modal, placeholder_text="Nome do Gasto")
        entrySaida.pack(pady=2)

        labelOpcaoGastos = customtkinter.CTkLabel(modal, text="Valor Gasto:", fg_color="transparent")
        labelOpcaoGastos.pack(pady=2)

        entryGastosIndicado = customtkinter.CTkEntry(modal, placeholder_text="Indique o valor Gasto")
        entryGastosIndicado.pack(pady=2)
        
        labelOpcaoParcelas = customtkinter.CTkLabel(modal, text="Parcelas:", fg_color="transparent")
        labelOpcaoParcelas.pack(pady=2)

        optionmenu_var = customtkinter.StringVar()
        arrayValorParcelas = []

        for i in range(25):
            arrayValorParcelas.append(str(i))
        
        optionmenuParcelas = customtkinter.CTkOptionMenu(modal,values=arrayValorParcelas,
                                         variable=optionmenu_var)
        optionmenuParcelas.pack(pady=5)

        
        labelPago = customtkinter.CTkLabel(modal, text="Indique o status de pagamento", fg_color="transparent")
        labelPago.pack(pady=2)

        switch_var = customtkinter.StringVar(value="Sim")
        switch = customtkinter.CTkSwitch(modal, text="Já está pago?",
                                 variable=switch_var, onvalue="Sim", offvalue="Não")

        switch.pack(pady=2)

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()

        add_button = customtkinter.CTkButton(modal, text="Inserir" )
        add_button.pack(pady=5)
       
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy )
        close_button.pack(pady=5)
    
    def editSaida(self):
        modal = tk.Toplevel()
        modal.title("Edição de Saida/Gastos")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

    def deleteSaida(self):
        modal = tk.Toplevel()
        modal.title("Exclusão de Saida/Gastos")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()

    def cadastroInvestimentos(self):
        modal = tk.Toplevel()
        modal.title("Inserção de Investimento")
        modal.geometry("800x600")

        labelTitle = customtkinter.CTkLabel(modal, text="Inserção de Investimentos", fg_color="transparent",font=("",23))
        labelTitle.pack(pady=5)

        labelNomeInvestmento = customtkinter.CTkLabel(modal,text="Nome do Investimento:")
        labelNomeInvestmento.pack(pady = 5 )
        entryNomeInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Nome Investimento")
        entryNomeInvestimento.pack(pady=5)

        labelTipoInvestmento = customtkinter.CTkLabel(modal,text="Tipo do Investimento:")
        labelTipoInvestmento.pack(pady = 5 )
        entryTipoInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Tipo Investimento")
        entryTipoInvestimento.pack(pady=5)
        
        labelValorInvestmento = customtkinter.CTkLabel(modal,text="Valor do Investimento:")
        labelValorInvestmento.pack(pady = 5 )
        entryValorInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Valor Investimento")
        entryValorInvestimento.pack(pady=5)

        labelRentabilidadeInvestmento = customtkinter.CTkLabel(modal,text="Rentabilidade do Investimento:")
        labelRentabilidadeInvestmento.pack(pady = 5 )
        entryRentabilidadeInvestimento = customtkinter.CTkEntry(modal,placeholder_text="Rentabilidade Investimento")
        entryRentabilidadeInvestimento.pack(pady=5)

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        add_button = customtkinter.CTkButton(modal, text="Inserir" )
        add_button.pack(pady=5)

        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
    
    def editInvestimentos(self):
        modal = tk.Toplevel()
        modal.title("Edição de Investimento")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)
    
    def deleteInvestimentos(self):
        modal = tk.Toplevel()
        modal.title("Exclusão de Investimento")
        modal.geometry("800x600")

        # Desabilita interação com a janela principal
        modal.transient()
        modal.grab_set()
        
        close_button = customtkinter.CTkButton(modal, text="Fechar", command=modal.destroy)
        close_button.pack(pady=10)

if __name__ == '__main__':
    root = customtkinter.CTk()
    app = TelaPrincipal(root)
    root.mainloop()