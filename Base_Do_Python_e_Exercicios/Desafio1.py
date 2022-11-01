# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
# entrada = input().split()

from os import sep


entrada = input(f'''Digite o valor do primeiro a distancia depois o primeiro lado diâmetro e depois 
digite o valor do segundo diametro.
''').split(sep=",",maxsplit=3)

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])



# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:

Calculo = distancia / (diametro1+diametro2)

print(f"{Calculo:.2f}")