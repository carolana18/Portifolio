
import tkinter as tk
from tkinter import messagebox
import cadastro as cad
import jogo  # Certifique-se de que o módulo do jogo está importado corretamente

class TelaPrincipal:
    def __init__(self): 
        # Inicializa a janela principal
        self.root = tk.Tk()
        self.root.title("Login")
        # Exibe a tela principal de login/cadastro
        self.exibirtelaprincipal()

    def exibirtelaprincipal(self):
        # Remove todos os componentes existentes na janela
        for componentes in self.root.winfo_children():
            componentes.destroy()

        # Adiciona um título à janela
        titulo = tk.Label(self.root, text="Faça seu login ou cadastro", font=("Arial", 16))
        titulo.pack(pady=10)

        # Adiciona um campo para o nick
        labelNick = tk.Label(self.root, text="Digite seu nick:")
        labelNick.pack(pady=(5, 0))
        self.entradaNick = tk.Entry(self.root, width=30)
        self.entradaNick.pack(pady=5)

        # Adiciona um campo para a senha
        labelSenha = tk.Label(self.root, text="Digite sua senha:")
        labelSenha.pack(pady=(5, 0))
        self.entradaSenha = tk.Entry(self.root, show="*", width=30)
        self.entradaSenha.pack(pady=5)

        # Adiciona um botão de login
        btnLogin = tk.Button(self.root, text="Entrar", command=self.verificarLogin)
        btnLogin.pack(pady=5)

        # Adiciona um botão de cadastro
        btnCadastro = tk.Button(self.root, text="Cadastrar", command=self.cadastrarUsuario)
        btnCadastro.pack(pady=5)

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





