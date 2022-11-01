#Importando a biblioteca
from itertools import groupby
import pandas as pd



PATH = f"datasets\Gapminder.csv"

#Lendo o arquivo csv 
# Passando o argumento error_bad_lines=False para True porque estou forçando a ele carregar
#Coluna nulas ou duplicadas , depois passo o sep= que seria o separador o arquivo

df = pd.read_csv(PATH,sep=';',error_bad_lines=False)

#Mostrando a primeiras linhas 
# é possivel passar parâmetros de quantidade de linha que eu desejo visualizar

# print(df.head(5))

#Renomeando as colunas 

df = df.rename(columns={"country":"Pais","continent":"continente","year":"ano","lifeExp":"Expectativa de vida","pop":"populacao","gp":"PIB"})

# print(df.head(10))

#Retorna dados estatisticos dos dados

# print(df.describe())

#Retorna os tipos de dados

# print(df.dtypes)


#Retornando a tabela de quantidades de continentes do pais 

# print(df.groupby("continente")["Pais"].nunique())

#Retornando a média da espectativa de vida 

# print(df.groupby("Expectativa de vida").mean())

#Retornando a média de  expectativa de vida por ano

print(df.groupby("ano")["Expectativa de vida"].mean())