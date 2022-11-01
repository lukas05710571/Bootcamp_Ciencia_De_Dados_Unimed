from select import POLLRDBAND
from tkinter import Place
from tkinter.tix import COLUMN
import pandas as pd

# Importando várias planilhas
dataset1 = pd.read_excel(r"datasets\Aracaju.xlsx")
dataset2 = pd.read_excel(r"datasets\Fortaleza.xlsx")
dataset3 = pd.read_excel(r"datasets\Natal.xlsx")
dataset4 = pd.read_excel(r"datasets\Recife.xlsx")
dataset5 = pd.read_excel(r"datasets\Salvador.xlsx")

#Analisando a quantidade de colunas e se caso se trata da mesma coisa

# print(dataset1.info)
# print(dataset2.info)
# print(dataset3.info)
# print(dataset4.info)

#concatenando as planilhas
plan_list = pd.concat([dataset1,dataset2,dataset3,dataset4,dataset5])

#Analisando quantas colunas e linhas eu tenho

# print(plan_list.shape)

#Exibindo as 5 primeiras linhas
# print(plan_list.head(5))

#Exibindo as 5 ultimas linhas da tabela
# print(plan_list.tail(5))

#Verificando a tipagem de dados

# print(plan_list.dtypes)

#Mudando a tipagem dos dados

# plan_list['LojaID'] = plan_list["LojaID"].astype(str)
# print(plan_list.dtypes)

#Procurando a quantidade de valores nulos na planilha

# print(plan_list.isnull().sum())

#Subtituindo valores nulos por zero

# plan_list['LojaID'].fillna(0,inplace=True)

#Apagando linhas de valores nulos
# plan_list.dropna(subset=["Vendas"],inplace=True)

#Removendo linhas que estão com valores faltantes em todas as colunas
# plan_list.dropna(how="all",inplace=True)


#Criando coluna de receitas
# plan_list["Receitas"] = plan_list["Vendas"].mul(plan_list["Qtde"])


#Retorna a maior quantidade de receita
# plan_list['Receitas'].max()

#Retorna o valor minimo de receita
# plan_list['Receitas'].min()

#nlargest localizando o top 3 das lojas que tiveram mais receita
# plan_list.nlargest(3,'Receitas')

#nsmallest localizando o top 3 das lojas que tiveram menas receita
# plan_list.nsmallest(3,'Receitas')

#Agrupamento do total de receitas por cada cidade
# plan_list.groupby("Cidade")["Receitas"].sum()

#Retornando o top 3 de cidades que mais faturaram
# plan_list.nlargest(3,"Receitas")

#Retornando as cidades que menos faturou
# plan_list.nsmallest(3,"Receitas")

#Ordenando o conjunto de dados na ordem do maior para o menor
# plan_list.sort_values("Receitas",ascending=False).head(10)

#Trabalhando com datas e transformando em string

# plan_list['Data'] = plan_list["Data"].astype(str)

#transformando em formato de data
# plan_list['Data'] = pd.to_datetime(plan_list['Data'])

#Agrupando o total da receita por ano
# plan_list.groupby(plan_list["Data"].dt.year)["Receitas"].sum()

#Amostra simples :
# plan_list.sample(10)

#Criando uma nova coluna com ano
# plan_list['Ano'] = plan_list['Data'].dt.year


#Extraindo dia e mês 
# plan_list['Dia'] , plan_list['Mes'] = plan_list['Data'].dt.day , plan_list['Data'].dt.month

#Retornando a data mais antiga
# plan_list["Data"].min()

#Retornando a diferença de dias
# plan_list['Diferença_Dias'] = plan_list['Data'] - plan_list['Data'].min()

#Criando coluna de trimestre
# plan_list['Trimestre'] = plan_list['Data'].dt.quarter

#Retorna quantas vezes essa loja vendeu na ordem de maior para menor
# filtro_vendas_março =  plan_list.loc[(plan_list['Data'].dt.year == 2019) & (plan_list['Data'].dt.month == 3)]

#Criar gráfico de barras
# plan_list['LojaID'].value_counts(ascending=False).plot.bar();

#Criando gráfico de Pizza mostrando o total da receita por ano
# plan_list.groupby(plan_list['Ano'])['Receitas'].sum().plot.pie();

#Total De Vendas por cidade
# plan_list['Cidade'].value_counts()


#Personalizando o gráfico e colocando titulo nos eixos
# import matplotlib.pyplot as plt

# plan_list['Cidade'].value_counts(ascending=True).plot.bar(title="Total de Vendas por Cidade");
# plt.xlabel("Cidades");
# plt.ylabel("Volume De Vendas");

#Alterando cor do gráfico
# plan_list['Cidade'].value_counts(ascending=True).plot.bar(title="Total de Vendas por Cidade",color="#d3d300");
# plt.xlabel("Cidades");
# plt.ylabel("Volume De Vendas");


#alterando o estilo do grafico
# Place.groupby(plan_list['Mes'])['Qtde'].sum().plot(title="Analise Quantidade De Vendas Por Mês");

# plt.xlabel("Mês")
# plt.ylabel("Quantidade")
# plt.style.use("ggplot")
# plt.legend();


#Quantidade de vendas de produtos
# plan_list.groupby(plan_list['Mes'])['Qtde'].sum().plot(title="Volume de vendas por mês");
# plt.xlabel("Mês Da Venda");
# plt.ylabel("Total De Produtos Vendidos");


#Selecionar apenas vendas de 2019
# Vendas_2019 = plan_list[plan_list['Ano'] == 2019]


#Total de produtos vendidos por mês
# Vendas_2019.groupby(Vendas_2019['Mes'])['Qtde'].sum().plot(marker= "o");
# plt.xlabel("Mês");
# plt.ylabel("Quantidade de Vendas");
# plt.legend();

#Histograma
# plt.hist(Vendas_2019['Mes'],Vendas_2019['Qtde'].sum())


