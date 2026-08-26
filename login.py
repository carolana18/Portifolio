
import tkinter as tk
from tkinter import messagebox
import cadastro as cad
import jogo  # Certifique-se de que o módulo do jogo está importado corretamente


#PALETA DE CORES

COR_BG = "#000000"
COR_TEXTO = "#FFF8BC"      # Amarelo/Creme suave
COR_BT_LOGIN = "#F3214E"   # Vermelho Vibrante
COR_BT_CAD = "#F4A854"     # Laranja/Dourado
COR_CAMPO_BG = "#222222"   # Escuro suave para a caixa de texto
COR_CAMPO_TEXT = "#FFF8BC" # Texto digitado
COR_DETALHE = "#CF023B"

class TelaPrincipal:
    def __init__(self): 
        # Inicializa a janela principal
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("380x420")
        self.root.configure(bg=COR_BG)
        self.root.resizable(False, False)
        # Exibe a tela principal de login/cadastro
        self.exibirtelaprincipal()

    def exibirtelaprincipal(self):
        # Remove todos os componentes existentes na janela
        for componentes in self.root.winfo_children():
            componentes.destroy()

        # Adiciona um título à janela
        titulo = tk.Label(self.root, text="Faça seu login ou cadastro", 
        font=("Arial", 16), 
        bg= COR_BG, 
        fg=COR_TEXTO)
        titulo.pack(pady=10)

        # Adiciona um campo para o nick
        labelNick = tk.Label(self.root, text="Digite seu nick:", 
        font=("Arial", 14),
        bg=COR_BG, 
        fg=COR_TEXTO)
        labelNick.pack(pady=(5, 2))

        self.entradaNick = tk.Entry(self.root, width=28, 
        font=("Arial", 11), 
        bg=COR_CAMPO_BG, 
        fg=COR_CAMPO_TEXT, 
        relief="solid", 
        bd=1)
        self.entradaNick.pack(pady=(0, 10), ipady=3)

        # Adiciona um campo para a senha
        labelSenha = tk.Label(self.root, text="Digite sua senha:", 
        font=("Arial", 11, "bold"), 
        bg=COR_BG, 
        fg=COR_TEXTO)
        labelSenha.pack(pady=(5, 2))

        self.entradaSenha = tk.Entry(self.root, 
        width=28, 
        font=("Arial", 11),
        show="*", 
        bg=COR_CAMPO_BG, 
        fg=COR_CAMPO_TEXT, 
        insertbackground=COR_TEXTO, 
        relief="solid", 
        bd=1)
        self.entradaSenha.pack(pady=(0, 20), ipady=3)

        # Adiciona um botão de login
        btnLogin = tk.Button(self.root, text="Entrar", 
        font=("Arial", 11, "bold"), 
        bg=COR_BT_LOGIN, 
        fg="#FFFFFF", 
        activebackground=COR_DETALHE, 
        activeforeground="#FFFFFF", 
        width=22, 
        relief="flat", 
        cursor="hand2", 
        command=self.verificarLogin)
        btnLogin.pack(pady=6, ipady=3)

        # Adiciona um botão de cadastro
        btnCadastro = tk.Button(self.root, text="Cadastrar", 
            font=("Arial", 11, "bold"), 
            bg=COR_BT_CAD, 
            fg="#000000", 
            activebackground="#E0933E", 
            activeforeground="#000000", 
            width=22, 
            relief="flat", 
            cursor="hand2",command=self.cadastrarUsuario)
        
        btnCadastro.pack(pady=6, ipady=3)

    def verificarLogin(self):
        # Obtém o nick e a senha inseridos pelo usuário
        nick = self.entradaNick.get()
        senha = self.entradaSenha.get()

        # Verifica se o nick e a senha estão corretos
        if nick in cad.cadastroJogadores and cad.cadastroJogadores[nick]["senha"] == senha:
            # Exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            # Fecha a tela de login
            self.root.destroy()
            # Inicia o jogo passando o nick do usuário
            jogo.iniciarJogo(nick)
        else:
            # Exibe uma mensagem de erro se o nick ou a senha estiverem incorretos
            messagebox.showerror("Erro", "Nick ou senha incorretos!")

    def cadastrarUsuario(self):
        # Obtém o nick e a senha inseridos pelo usuário
        nick = self.entradaNick.get()
        senha = self.entradaSenha.get()

        # Verifica se o nick ou a senha estão vazios
        if not nick or not senha:
            # Exibe uma mensagem de erro se algum dos campos estiver vazio
            messagebox.showerror("Erro", "Nick e senha não podem estar vazios!")
            return

        # Verifica se o nick já está cadastrado
        if nick in cad.cadastroJogadores:
            # Exibe uma mensagem de erro se o nick já estiver cadastrado
            messagebox.showerror("Erro", "Nick já cadastrado!")
        else:
            # Cadastra o novo usuário
            cad.cadastroJogadores[nick] = {"senha": senha}
            # Salva as informações do usuário no arquivo de cadastro
            cad.salvarUsu(cad.cadastroJogadores)
            # Exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            # Fecha a tela de cadastro
            self.root.destroy()
            # Inicia o jogo passando o nick do usuário
            jogo.iniciarJogo(nick)

if __name__ == "__main__":
    # Cria uma instância da classe TelaPrincipal e inicia o loop principal da interface gráfica
    app = TelaPrincipal()
    app.root.mainloop()




