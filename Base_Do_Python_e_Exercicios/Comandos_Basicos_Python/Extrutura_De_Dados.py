# ** Manipulando Listas**

# ---







# # Criando array
# animais = ["Leão","Cobra","Macaco","Girafa"]

# animais

# #Adicionando itens na lista
# animais.append("Morcego")

# animais

# #Substituindo dados da Array por posição
# animais[0] = "Golfinho"
# animais[1] = "Tubarão"
# animais[2] = "Cachorro"
# animais[3] = "Gato"
# animais

# #Função que retorna o tamanho da array
# len(animais)

# #Removendo Informações da lista por nome
# animais.remove("Morcego")
# animais

# #Pesquisa se contém ou não o valor desejado na lista
# "Morcego" in animais

# #Metodo que retorna quantas vezes esse caracterer aparece na lista
# animais.count("Morcego")

# #Metodo para adicionar uma lista aninhada : Melhor dizendo eu estou extendendo a lista criando novas
# animais.extend(["Nome","Sobrenome","Preço"])

# animais

# #Atribuindo valores a lista
# Lista_Compras = {"Pera":20,"Banana":30}


# Lista_Compras

# #Listando valores da lista
# Lista_Compras["Pera"]

# #Cria chaves especiais para as listas e também é possivel já adicionar valor a lista.
# Lista_Compras.fromkeys("ABC",30)

# #Esse função lista dos valores da array
# Lista_Compras.values()

# # O metodo keys retorna as chaves da lista
# Lista_Compras.keys()

# # Seta uma chave na lista e o valor dessa chave
# Lista_Compras.setdefault('Uva',80)

# Lista_Compras

# # Com base da chave na array utilizando o metodo update eu posso atualizar o valor da lista
# Lista_Compras.update({"Uva":90})
# Lista_Compras

# # Tuplas

# ---



# # Criando lista imutável
# Valores = (300,90,30,60,20)

# # Função que retorna o maior valor da lista
# max(Valores)

# #Função que retorna o menir valor da lista
# min(Valores)

# #Função que ordena os dados podendo receber parametros para listas do maior para o menor ou ao inverso.
# sorted(Valores)