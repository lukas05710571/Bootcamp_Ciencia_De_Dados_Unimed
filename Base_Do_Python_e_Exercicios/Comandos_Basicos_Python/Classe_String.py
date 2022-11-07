
# Seria uma algoritmo para manipulação simples com a tipagem string
# Segundo os ensinamentos o tipo string é tratado de forma literal no python 
# Isso Significa que existem inúmeros métodos especificos para o dados do tipo string
# Ao manipular uma string ela é visto como um objeto em python com sua classe e métodos.


nome = "  lukas de oliveira  "
print(len(nome))

# Retorna em maisculo
print(nome.upper())
# Retorna em minusculo
print(nome.lower())
# Retorna A primeira letra em maiusculo
print(nome.title())
print(len(nome))
# Excluindo espaçamentos
print(nome.strip())



#incluindo caracter em ambos lados
print(nome.center(25,"#"))
#Retorna o tamanho da cadeia de caracteres atualmente
print(len(nome))

# Inclui Caracter ao lado direito
print(nome.ljust(21,"#"))
print(len(nome))

#Inclui caracter no lado esquerdo
print(nome.rjust(22,"_"))

# Unindo uma string com numero e convertendo ambos dados em string 
print(nome.strip())
print('_'.join(nome))
# Unindo apenas no começo e no final da string
print(nome.join('__'))

