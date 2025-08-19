import json # Importa o módulo para manipular arquivos JSON
import os # Importa o módulo para interagir com o sistema de arquivos

# Nome do arquivo onde o ranking será armazenado
ARQ_RANKING = 'ranking.json'

# Verifica se o arquivo de ranking existe
if not os.path.exists(ARQ_RANKING):
    # Caso o arquivo não exista, cria um novo arquivo
    # Inicializa o arquivo com um dicionário contendo listas vazias para cada nível de dificuldade
    with open(ARQ_RANKING, 'w') as f:
        json.dump({"facil": [], "medio": [], "dificil": []}, f)

# Função para carregar os dados do ranking do arquivo JSON
def carregarRanking():
    try:
        # Tenta abrir o arquivo de ranking em modo de leitura
        with open(ARQ_RANKING, 'r') as f:
            return json.load(f) # Retorna os dados do ranking como um dicionário
    except (FileNotFoundError, json.JSONDecodeError):
        # Caso o arquivo não exista ou esteja corrompido, retorna o formato padrão
        return {"facil": [], "medio": [], "dificil": []}

# Função para salvar os dados do ranking no arquivo JSON
def salvarRanking(ranking):
    with open(ARQ_RANKING, 'w') as f:
        # Grava o dicionário de ranking no arquivo com formatação legível (indentação)
        json.dump(ranking, f, indent=4)

# Carrega o ranking ao iniciar o programa
ranking = carregarRanking()
