import os # Módulo para lidar com funcionalidades do sistema operacional
import json # Módulo para manipulação de dados em formato JSON

# Nome do arquivo onde os dados de cadastro serão armazenados
ARQCADASTRO = 'cadastro.json'

# Verifica se o arquivo de cadastro já existe no sistema
if not os.path.exists(ARQCADASTRO):
    # Se o arquivo não existe, cria um novo arquivo vazio com um dicionário vazio
    with open(ARQCADASTRO, 'w') as f:
        json.dump({}, f) # Grava um dicionário vazio no arquivo

# Função para carregar os dados de usuários do arquivo JSON
def carregarUsu():
    try:
        # Tenta abrir e carregar os dados do arquivo de cadastro
        with open(ARQCADASTRO, 'r') as f:
            return json.load(f)  # Retorna os dados como um dicionário
    except (FileNotFoundError, json.JSONDecodeError):
        # Caso o arquivo não seja encontrado ou esteja corrompido, retorna um dicionário vazio.
        return {}

# Função para salvar os dados de usuários no arquivo JSON
def salvarUsu(cadastro):
    with open(ARQCADASTRO, 'w') as f:
        # Grava o dicionário de cadastro no arquivo, com formatação legível (indentação)
        json.dump(cadastro, f, indent=4)

# Carrega os dados de cadastro existentes no início do programa
cadastroJogadores = carregarUsu()

