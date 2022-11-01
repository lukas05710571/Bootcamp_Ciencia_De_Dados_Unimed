
# Fatiamento : Serve para localizar valores string a partir da sua posição
# Pois de forma literal ele cria posicionamento de cada caracter onde é possivel ,
# escolher qual posição deseja listar podendo definiar start,stop,step

Nome = "Lukas De Oliveira Almeida"

print(Nome[0])
# Imprimi L

print(Nome[2])
# Implime K

print(Nome[1:5])
#Imprime ukas

print(Nome[:5])
#Imprime Lukas 

print(Nome[9:25])
#Imprime Oliveira Almeida

# Start , Stop , Step
print(Nome[:5:2])
#Imprime LKS

print(Nome[:])
#Imprime todo o arranjo de caracteres do tipo String

print(Nome[::-1])
#Imprime um espelo da string porém ao contrário