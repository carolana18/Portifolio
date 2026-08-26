import tkinter as tk # Biblioteca para criar interfaces gráficas
from tkinter import messagebox # Biblioteca para exibir mensagens
import random # Biblioteca para gerar valores aleatórios
import ranking  # Importando o módulo de ranking

#PALETA DE CORES

COR_BG =  "#333333"         # Preto
COR_TEXTO = "#FFF8BC"      # Amarelo/Creme suave
COR_BT_FACIL = "#F4A854"   # Laranja/Dourado
COR_BT_MEDIO = "#F3214E"   # Vermelho Vibrante
COR_BT_DIFICIL = "#CF023B" # Vermelho Escuro
COR_CELULA_VAZIA = "#FFF8BC"  # Amarelo Creme (botão do tabuleiro antes de clicar)
COR_CELULA_CERTA = "#333333"  # Vermelho Vibrante ao acertar a célula
COR_CELULA_ERRADA = "#F3214E"

DESENHOS = {
    "facil": [

        #coracao
        [
            [0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]
        ], 
        #sorriso
        [
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0]

        ],
        #casa
        [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0]
        ],
        #arvore
        [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ],
        #barco a vela
        [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1]
        ],
        #pato
        [
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0]
        ],

        #maca
        [
           [0, 0, 1, 1, 0],
           [0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [0, 1, 0, 1, 0]
        ],
        #seta
        [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0]
        ]
    ],
    "medio": [
        #espada
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],

        #fantasma
        [
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
        ],

        #cogumelo
        [
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
        ],

        #pacman
        [
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
        ],

        #nota musical
        [
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 0]
        ],

        #ancora
        
        [
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
        ],

        #chave 
        [
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        ],

        #caveira
        [
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
        ]
    ],

    "dificil": [
        #espada
        [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ],
        #gamepad
        [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1],
            [1,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,0,1,0,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,0,1,0,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
            [0,1,1,1,0,0,0,0,0,0,0,1,1,1,0],
            [0,1,1,1,0,0,0,0,0,0,0,1,1,1,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ],

        #castelo
        [
            [1,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
            [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
            [1,1,1,1,1,0,0,1,0,0,1,1,1,1,1],
            [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,1,1,1,1,1,1,1,0,0,1,1],
            [1,1,0,0,1,1,1,1,1,1,1,0,0,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1]
        ],

        #caveira
        [
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        ],

        #rocket
        [
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
        ],

        #ancora
        [
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        ]
    ]

}
class NonogramJogo:
    def __init__(self, root, tamanho, nick):
        self.root = root # Janela principal
        self.root.configure(bg=COR_BG)
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
        frameMenu = tk.Frame(self.root, bg=COR_BG)
        frameMenu.pack(padx=20, pady=20)
        tk.Label(frameMenu, text="Escolha o nível de dificuldade", 
        font=("Arial", 14),
        bg=COR_BG,
        fg=COR_TEXTO).pack(pady=(0, 15))
        # Botões para selecionar o nível de dificuldade
        btnFacil = tk.Button(frameMenu, text="Nível Fácil", 
        font=("Arial", 11, "bold"),
        bg=COR_BT_FACIL,
        fg="#000000",
        cursor="hand2",
        relief="flat",
        command=lambda: self.iniciarJogo(5, "facil"))

        btnFacil.pack(fill='x', pady=5, ipady=3)
        btnMedio = tk.Button(frameMenu, text="Nível Médio", 
        font=("Arial", 11, "bold"),
        bg=COR_BT_MEDIO,
        fg="#FFFFFF",
        cursor="hand2",
        relief="flat",
        command=lambda: self.iniciarJogo(10, "medio"))
        btnMedio.pack(fill='x', pady=5, ipady=3)

        btnDificil = tk.Button(frameMenu, text="Nível Difícil", 
        font=("Arial", 11, "bold"),
        bg=COR_BT_DIFICIL,
        fg="#FFFFFF",
        cursor="hand2",
        relief="flat",
        command=lambda: self.iniciarJogo(15, "dificil"))
        btnDificil.pack(fill='x', pady=5, ipady=3)

        # Botão para acessar o ranking
        btnRanking = tk.Button(frameMenu, text="Ver Ranking", 
        font=("Arial", 11, "bold"),
        bg=COR_TEXTO,
        fg="#000000",
        cursor="hand2",
        relief="flat",
        command=self.abrirRanking)
        btnRanking.pack(fill='x', pady=(15, 5), ipady=3)
        # Botão para sair do jogo
        btnSair = tk.Button(frameMenu, text="Sair", 
        font=("Helvetica", 11, "bold"),
        bg="#222222",
        fg=COR_TEXTO,
        cursor="hand2",
        relief="flat",
        command=self.root.quit)
        btnSair.pack(fill='x', pady=5, ipady=3)

    def abrirRanking(self):
    # Abre uma janela com o ranking dos jogadores
        ranking_window = tk.Toplevel(self.root) # Janela separada
        ranking_window.title("Ranking")
        ranking_window.configure(bg=COR_BG)
        ranking_window.geometry("300x400")
        # Frame para organizar os dados do ranking
        frameRanking = tk.Frame(ranking_window, bg=COR_BG)
        frameRanking.pack(padx=15, pady=15, fill="both", expand=True)
        # Carrega os dados do ranking
        ranking_data = ranking.carregarRanking()
        tk.Label(frameRanking, text="Ranking:", 
        font=("Arial", 12),
        bg=COR_BG,
        fg=COR_TEXTO).pack(pady=10)
        # Exibe o ranking por níveis (fácil, médio e difícil)
        for nivel in ["facil", "medio", "dificil"]:
            tk.Label(frameRanking, text=nivel.capitalize(), 
                font=("Arial", 12, "bold"),
                bg=COR_BG,
                fg=COR_BT_FACIL,
                ).pack(pady=(5, 2))
            if nivel in ranking_data and ranking_data[nivel]:
                for i in range(len(ranking_data[nivel][:5])):
                    record = ranking_data[nivel][i]
                    texto = f"{i + 1}. {record['nick']} - {record['tempo']}s"
                    tk.Label(
                        frameRanking,
                        text=texto,
                        font=("Helvetica", 10),
                        bg=COR_BG,
                        fg=COR_TEXTO
                    ).pack()
            else:
                tk.Label(
                    frameRanking,
                    text="Sem registros",
                    font=("Helvetica", 9, "italic"),
                    bg=COR_BG,
                    fg="#888888"
                ).pack()
        # Botão para fechar a janela de ranking
        btnFechar = tk.Button(frameRanking, 
            text="Fechar", 
            font=("aArial", 10, "bold"),
            bg=COR_BT_MEDIO,
            fg="#FFFFFF",
            cursor="hand2",
            relief="flat",
            command=ranking_window.destroy)
        btnFechar.pack(pady=15, ipady=2)

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
        self.solucao = random.choice(DESENHOS[self.nivel])
        self.tamanho = len(self.solucao)
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
        # Limpa elementos anteriores da tela
        for componente in self.root.winfo_children():
            componente.destroy()

        # Frame Principal Centralizado
        frameTabuleiro = tk.Frame(self.root, bg=COR_BG)
        frameTabuleiro.pack(expand=True, pady=10)

        max_dicas_col = max(len(d) for d in self.dicasColunas) if self.dicasColunas else 1
        max_dicas_lin = max(len(d) for d in self.dicasLinhas) if self.dicasLinhas else 1

        # ---------------------------------------------------------
        # 1. Células vazias (Canto Superior Esquerdo)
        # ---------------------------------------------------------
        for r in range(max_dicas_col):
            for c in range(max_dicas_lin):
                tk.Label(
                    frameTabuleiro,
                    text="",
                    bg="#D9D9D9",
                    relief="solid",
                    bd=1,
                    width=3,
                    height=1
                ).grid(row=r, column=c, sticky="nsew")

        # ---------------------------------------------------------
        # 2. Dicas das Colunas (Topo)
        # ---------------------------------------------------------
        for col_idx, dica in enumerate(self.dicasColunas):
            numeros = dica if dica else [0]
            offset = max_dicas_col - len(numeros)
            
            for row_idx in range(max_dicas_col):
                num_texto = str(numeros[row_idx - offset]) if row_idx >= offset else ""

                tk.Label(
                    frameTabuleiro,
                    text=num_texto,
                    font=("Helvetica", 9, "bold"),
                    bg="#D9D9D9",
                    fg="#000000",
                    relief="solid",
                    bd=1,
                    width=3,
                    height=1
                ).grid(row=row_idx, column=max_dicas_lin + col_idx, sticky="nsew")

        # ---------------------------------------------------------
        # 3. Dicas das Linhas (Esquerda) e Tabuleiro
        # ---------------------------------------------------------
        for lin_idx, dica in enumerate(self.dicasLinhas):
            numeros = dica if dica else [0]
            offset = max_dicas_lin - len(numeros)

            # Células de dicas das linhas
            for col_idx in range(max_dicas_lin):
                num_texto = str(numeros[col_idx - offset]) if col_idx >= offset else ""

                tk.Label(
                    frameTabuleiro,
                    text=num_texto,
                    font=("Helvetica", 9, "bold"),
                    bg="#D9D9D9",
                    fg="#000000",
                    relief="solid",
                    bd=1,
                    width=3,
                    height=1
                ).grid(row=max_dicas_col + lin_idx, column=col_idx, sticky="nsew")

            # Botões do Tabuleiro (Mesmo tamanho visual das dicas)
            linha_botoes = []
            for col_idx in range(self.tamanho):
                btn = tk.Button(
                    frameTabuleiro,
                    text="",
                    bg=COR_CELULA_VAZIA,
                    activebackground=COR_BT_FACIL,
                    relief="raised",
                    bd=1,
                    width=3,      # Mesma largura de texto (3 caracteres)
                    height=1,     # Mesma altura
                    cursor="hand2",
                    command=lambda x=lin_idx, y=col_idx: self.marcarCelula(x, y)
                )
                btn.grid(row=max_dicas_col + lin_idx, column=max_dicas_lin + col_idx, padx=1, pady=1, sticky="nsew")
                linha_botoes.append(btn)
            self.botoes.append(linha_botoes)

        # ---------------------------------------------------------
        # RÓTULO DE TEMPO E BOTÃO SAIR
        # ---------------------------------------------------------
        self.labelTempo = tk.Label(
            self.root,
            text="Tempo: 00:00",
            font=("Helvetica", 11, "bold"),
            bg=COR_BG,
            fg=COR_TEXTO
        )
        self.labelTempo.pack(pady=5)

        btnSair = tk.Button(
            self.root,
            text="Voltar ao Menu",
            font=("Helvetica", 10, "bold"),
            bg=COR_BT_FACIL,
            fg="#000000",
            relief="flat",
            cursor="hand2",
            command=self.exibirMenuInicial
        )
        btnSair.pack(pady=10, ipady=2)

        if self.iniciarCronometro:
            self.atualizarCronometro()

    def atualizarCronometro(self):
        if self.jogoAtivo and hasattr(self, 'labelTempo') and self.labelTempo.winfo_exists():
            self.tempo += 1
            minutos = self.tempo // 60
            segundos = self.tempo % 60
            self.labelTempo.config(text=f"Tempo: {minutos:02d}:{segundos:02d}")
            self.root.after(1000, self.atualizarCronometro)

    def marcarCelula(self, x, y):
        if not self.jogoAtivo:
            return

        btn = self.botoes[x][y]
        if self.solucao[x][y] == 1:
            btn.config(bg=COR_CELULA_CERTA, state="disabled")
        else:
            btn.config( 
                       state="disabled" , text="X",                # Desenha o 'X'
                       fg="#F3214E",            # Cor Vermelha do 'X'
                       font=("Arial", 9, "bold"),
                       relief="sunken")
            self.verificarErro(x, y)

        self.verificarVitoria()

    def verificarErro(self, x, y):
        #if self.solucao[x][y] == 0:
            # messagebox.showerror("Erro", "Você cometeu um erro!")
         pass

    def verificarVitoria(self):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                # Se uma célula correta não possui a cor de acerto, ainda não venceu
                if self.solucao[i][j] == 1 and self.botoes[i][j].cget("bg") != COR_CELULA_CERTA:
                    return

        self.jogoAtivo = False
        messagebox.showinfo("Vitória", f"Você ganhou! Tempo: {self.tempo} segundos")
        self.atualizarRanking()
        self.exibirMenuInicial()

    def atualizarRanking(self):
        ranking_data = ranking.carregarRanking()
        if self.nivel not in ranking_data:
            ranking_data[self.nivel] = []

        ranking_data[self.nivel].append({"nick": self.nick, "tempo": self.tempo})
        ranking_data[self.nivel] = sorted(ranking_data[self.nivel], key=lambda x: x["tempo"])[:5]
        ranking.salvarRanking(ranking_data)


def iniciarJogo(nick):
    root = tk.Tk()
    root.title("Jogo Nonogram")
    root.configure(bg=COR_BG)
    jogo = NonogramJogo(root, tamanho=5, nick=nick)
    root.mainloop()
