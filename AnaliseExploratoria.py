import pandas as pd

# Leitura do arquivo com separador correto
csv_path = "./dados/baseComentarios.csv"
df = pd.read_csv(csv_path, sep=';')

# Mostrar as 5 primeiras linhas
print("### 5 primeiras linhas ###")
print(df.head())

# Informações gerais (colunas, tipos de dados, não nulos)
print("\n### Informações gerais do DataFrame ###")
print(df.info())

# Estatísticas descritivas para colunas numéricas
print("\n### Estatísticas descritivas (numéricas) ###")
print(df.describe())

# Estatísticas para colunas texto (comentarios)
print("\n### Estatísticas para colunas texto ###")
print(df['comentario'].describe())

# Contagem de valores nulos por coluna
print("\n### Contagem de valores nulos ###")
print(df.isnull().sum())

# Verificar se existem valores duplicados
print("\n### Quantidade de linhas duplicadas ###")
print(df.duplicated().sum())