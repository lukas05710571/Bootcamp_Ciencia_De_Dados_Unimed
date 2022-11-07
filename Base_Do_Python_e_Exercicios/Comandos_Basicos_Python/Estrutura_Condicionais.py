
from datetime import date

print("Algoritimo para saber se você é de maior ou não \n")
Age = int(input("Digite o ano em que nasceu \n"))

Ano_Atual = 2022

Calculo = Ano_Atual - Age

# Operador ternário.
Resultado = "Você é maior de idade.\n" if Calculo >= 18 else "Você ainda é de menor.\n"

print(Resultado)

