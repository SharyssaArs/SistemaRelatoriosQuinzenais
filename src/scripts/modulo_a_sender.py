from dotenv import load_dotenv
import pandas as pd
import os

# Carrega as configurações do arquivo que está em config/.env
# Usa o diretório do script como referência para encontrar o .env
script_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_dir, '../../config/.env')
load_dotenv(dotenv_path)

# Pega o caminho salvo no .env
caminho_dados = os.getenv('PATH_DATA')

# Verifica se a variável foi carregada
if caminho_dados is None:
    print(f"Erro: PATH_DATA não foi encontrado em {dotenv_path}")
    exit(1)

# Constrói o caminho absoluto do arquivo de dados
data_path = os.path.join(script_dir, '../../' + caminho_dados)
data_path = os.path.abspath(data_path)

# Lê o arquivo
df = pd.read_csv(data_path)

#Visualiza as primeiras linhas
print(df.head())
