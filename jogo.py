import tkinter as tk # Biblioteca para criar interfaces gráficas
from tkinter import messagebox # Biblioteca para exibir mensagens
import random # Biblioteca para gerar valores aleatórios
import ranking  # Importando o módulo de ranking

class NonogramJogo:
    def __init__(self, root, tamanho, nick):
        self.root = root # Janela principal
        self.tamanho = tamanho # Tamanho do tabuleiro
        self.nick = nick # Apelido do jogador
        self.botoes = [] # Lista para armazenar os botões do tabuleiro
        self.tempo = 0 # Tempo do jogo
        self.iniciarCronometro = False # Controle do cronômetro
        self.solucao = [] # Matriz com a solução do jogo
        self.dicasLinhas = [] # Dicas para as linhas
        self.dicasColunas = [] # Dicas para as colunas
        self.jogoAtivo = True # Controle para verificar se o jogo está ativo
        self.exibirMenuInicial() # Exibe o menu inicial

    def exibirMenuInicial(self):
    # Exibe o menu inicial com opções de dificuldade e acesso ao ranking
        for componentes in self.root.winfo_children():  # Remove quaisquer elementos existentes na janela
            componentes.destroy()
        # Frame para organizar os botões do menu
        frameMenu = tk.Frame(self.root)
        frameMenu.pack(padx=10, pady=10)
        tk.Label(frameMenu, text="Escolha o nível de dificuldade", font=("Arial", 14)).pack(pady=10)
        # Botões para selecionar o nível de dificuldade
        btnFacil = tk.Button(frameMenu, text="Nível Fácil", command=lambda: self.iniciarJogo(5, "facil"))
        btnFacil.pack(fill='x', pady=5)
        btnMedio = tk.Button(frameMenu, text="Nível Médio", command=lambda: self.iniciarJogo(7, "medio"))
        btnMedio.pack(fill='x', pady=5)
        btnDificil = tk.Button(frameMenu, text="Nível Difícil", command=lambda: self.iniciarJogo(10, "dificil"))
        btnDificil.pack(fill='x', pady=5)
        # Botão para acessar o ranking
        btnRanking = tk.Button(frameMenu, text="Ver Ranking", command=self.abrirRanking)
        btnRanking.pack(fill='x', pady=5)
        # Botão para sair do jogo
        btnSair = tk.Button(frameMenu, text="Sair", command=self.root.quit)
        btnSair.pack(fill='x', pady=5)

    def abrirRanking(self):
    # Abre uma janela com o ranking dos jogadores
        ranking_window = tk.Toplevel(self.root) # Janela separada
        ranking_window.title("Ranking")
        # Frame para organizar os dados do ranking
        frameRanking = tk.Frame(ranking_window)
        frameRanking.pack(padx=10, pady=10)
        # Carrega os dados do ranking
        ranking_data = ranking.carregarRanking()
        tk.Label(frameRanking, text="Ranking:", font=("Arial", 12)).pack(pady=10)
        # Exibe o ranking por níveis (fácil, médio e difícil)
        for nivel in ["facil", "medio", "dificil"]:
            tk.Label(frameRanking, text=nivel.capitalize(), font=("Arial", 12)).pack()
            for i in range(len(ranking_data[nivel][:5])): # Mostra os 5 melhores tempos de cada nível
                record = ranking_data[nivel][i]
                texto = f"{i + 1}. {record['nick']} - {record['tempo']} segundos"
                tk.Label(frameRanking, text=texto, font=("Arial", 10)).pack()
        # Botão para fechar a janela de ranking
        btnFechar = tk.Button(frameRanking, text="Fechar", command=ranking_window.destroy)
        btnFechar.pack(pady=10)

    def iniciarJogo(self, tamanho, nivel):
         # Inicializa o jogo com o tabuleiro baseado no tamanho e no nível selecionado
        self.tamanho = tamanho
        self.nivel = nivel
        self.tempo = 0
        self.iniciarCronometro = True # Ativa o cronômetro
        self.botoes.clear() # Limpa os botões antigos
        self.jogoAtivo = True # Marca o jogo como ativo
        self.criarTabuleiro() # Gera o tabuleiro com solução e dicas
        self.exibirJogo() # Exibe o tabuleiro na interface

    def criarTabuleiro(self):
        # Gera a solução do tabuleiro e calcula as dicas de linhas e colunas
        self.solucao = [[random.choice([0, 1]) for _ in range(self.tamanho)] 
                        for _ in range(self.tamanho)]
        self.dicasLinhas = self.gerarDicas(self.solucao) # Calcula as dicas das linhas

        # Calcula as dicas das colunas
        self.dicasColunas = []
        for coluna in range(self.tamanho):
            dica = []
            contador = 0
            for linha in range(self.tamanho):
                if self.solucao[linha][coluna] == 1:
                    contador += 1
                elif contador > 0:
                    dica.append(contador)
                    contador = 0
            if contador > 0:
                dica.append(contador)
            self.dicasColunas.append(dica)

    def gerarDicas(self, tabuleiro):
        # Calcula as dicas de preenchimento para cada linha do tabuleiro
        dicas = []
        for linha in tabuleiro:
            dica = []
            contador = 0
            for celula in linha:
                if celula == 1:
                    contador += 1
                elif contador > 0:
                    dica.append(contador)
                    contador = 0
            if contador > 0:
                dica.append(contador)
            dicas.append(dica)
        return dicas

    def exibirJogo(self):
        for componentes in self.root.winfo_children():
            componentes.destroy()

        # Cria um frame para organizar o tabuleiro do jogo.
        frameTabuleiro = tk.Frame(self.root)
        frameTabuleiro.pack(padx=10, pady=10)

        # Adiciona as dicas das colunas (parte superior do tabuleiro)
        for i in range(len(self.dicasColunas)):
            coluna = self.dicasColunas[i]
            dica_texto = ""
            if coluna:
                # Concatena os números das dicas da coluna, separados por espaços
                for num in coluna:
                    dica_texto += str(num) + " "
                dica_texto = dica_texto.strip()
            else:
                # Caso não haja dicas, exibe "0".
                dica_texto = "0"
            # Cria um rótulo para exibir as dicas e posiciona na linha 0 (cabeçalho das colunas)
            tk.Label(frameTabuleiro, text=dica_texto, width=5).grid(row=0, column=i+1)

        # Adiciona as dicas das linhas (à esquerda do tabuleiro)
        for i in range(len(self.dicasLinhas)):
            linha = self.dicasLinhas[i]
            dica_texto = ""
            if linha:
                # Concatena os números das dicas da linha, separados por espaços
                for num in linha:
                    dica_texto += str(num) + " "
                dica_texto = dica_texto.strip()
            else:
                # Caso não haja dicas, exibe "0"
                dica_texto = "0"
            # Cria um rótulo para exibir as dicas e posiciona na coluna 0
            tk.Label(frameTabuleiro, text=dica_texto, width=5).grid(row=i+1, column=0)

        # Cria os botões do tabuleiro e os organiza no grid
        for i in range(self.tamanho):
            linha_botoes = [] # Lista para armazenar os botões da linha atual
            for j in range(self.tamanho):
                # Cria um botão para cada célula do tabuleiro, com fundo branco por padrão
                btn = tk.Button(frameTabuleiro, width=3, height=2, bg="white", command=lambda x=i, y=j: self.marcarCelula(x, y)) # Ação ao clicar na célula
                btn.grid(row=i+1, column=j+1, padx=0, pady=0, sticky="nsew") # Posiciona o botão no grid
                linha_botoes.append(btn) # Adiciona o botão à linha atual
            self.botoes.append(linha_botoes) # Adiciona a linha ao tabuleiro

         # Configura o layout para redimensionar as células do tabuleiro proporcionalmente
        for i in range(self.tamanho + 1):
            frameTabuleiro.grid_rowconfigure(i, weight=1)
            frameTabuleiro.grid_columnconfigure(i, weight=1)
        # Adiciona um rótulo para exibir o tempo decorrido do jogo
        self.labelTempo = tk.Label(self.root, text="Tempo: 00:00")
        self.labelTempo.pack()

        # Adiciona um botão para sair e retornar ao menu inicial
        btnSair = tk.Button(self.root, text="Sair", command=self.exibirMenuInicial)
        btnSair.pack(pady=10)
        # Inicia o cronômetro do jogo, se necessário
        if self.iniciarCronometro:
            self.atualizarCronometro()
#IMPORTANTE
    def atualizarCronometro(self):
         # Verifica se o jogo está ativo e se o rótulo do tempo ainda existe
        if self.jogoAtivo and self.labelTempo.winfo_exists():
            # Incrementa o tempo em 1 segundo
            self.tempo += 1
            minutos = self.tempo // 60 # Calcula os minutos
            segundos = self.tempo % 60 # Calcula os segundos restantes
            # Atualiza o rótulo com o novo tempo
            self.labelTempo.config(text=f"Tempo: {minutos:02}:{segundos:02}")
            # Agenda a próxima chamada desta função em 1 segundo
            self.root.after(1000, self.atualizarCronometro)
#IMPORTANTE
    def marcarCelula(self, x, y):
        # Impede ações caso o jogo tenha terminado
        if not self.jogoAtivo:
            return
        # Obtém o botão correspondente à célula clicada
        btn = self.botoes[x][y]
        if self.solucao[x][y] == 1:
            # Se a célula está correta, muda a cor para preto
            btn.config(bg="black")
        else:
            # Se a célula está incorreta, muda a cor para vermelho
            btn.config(bg="red")
            # Verifica se houve erro e se a vitória foi alcançada
        self.verificarErro(x, y)
        self.verificarVitoria()
#IMPORTANTE
    def verificarErro(self, x, y):
        # Se a célula clicada está incorreta, exibe uma mensagem de erro
        if self.solucao[x][y] == 0:
            messagebox.showerror("Erro", "Você cometeu um erro!")
#IMPORTANTE
    def verificarVitoria(self):
        # Verifica se todas as células corretas foram marcadas
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                # Se uma célula correta não foi marcada, ainda não há vitória
                if self.botoes[i][j].cget("bg") != "black" and self.solucao[i][j] == 1:
                    return
        # Se todas as células corretas foram marcadas, o jogador vence
        self.jogoAtivo = False # Desativa o jogo
        messagebox.showinfo("Vitória", f"Você ganhou! Tempo: {self.tempo} segundos")
        # Atualiza o ranking com o tempo do jogador e retorna ao menu inicial
        self.atualizarRanking()
        self.exibirMenuInicial()

    def atualizarRanking(self):
        # Carrega os dados do ranking existente
        ranking_data = ranking.carregarRanking()
        # Adiciona o tempo atual ao ranking do nível correspondente
        ranking_data[self.nivel].append({"nick": self.nick, "tempo": self.tempo})
        # Ordena o ranking pelo tempo e mantém apenas os 5 melhores tempos
        ranking_data[self.nivel] = sorted(ranking_data[self.nivel], key=lambda x: x["tempo"])[:5]  
         # Salva os dados do ranking atualizado
        ranking.salvarRanking(ranking_data)

def iniciarJogo(nick):
    # Inicializa a janela principal do jogo
    root = tk.Tk()
    root.title("Jogo Nonogram")
    # Cria uma instância do jogo, passando a janela, tamanho do tabuleiro e o apelido do jogador
    jogo = NonogramJogo(root, tamanho=5, nick=nick)
    # Inicia o loop principal da interface gráfica
    root.mainloop()
