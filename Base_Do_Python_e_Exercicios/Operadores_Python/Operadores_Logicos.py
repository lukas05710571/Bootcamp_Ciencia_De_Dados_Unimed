from ast import Not
from operator import not_


saldo = 1600
limite = 300
conta_especial = True
Saque_minimo_Terminal = 20

opcao = int(input("Digite a opção desejada \n 1 - Saque \n 2- Crédito/Empréstimo \n"))

if opcao == 1:

    operacao = int(input("Digite o valor que deseja sacar : \n Saque minino de 20 reais \n"))
    
    if operacao<=saldo and operacao >= Saque_minimo_Terminal :
        saldo -= operacao 
        print(f"Total do saque : R$:{operacao}")
    
    else:  print("Valor minimo é de 20 reais reinicie e tente novamente")

elif opcao == 2 and not conta_especial == False:
        
    print("Limite disponivel : R$",limite,"\n")
    operacao = int(input("Deseja sacar o valor ? \n 1- Sim / 2- Não\n"))
    if operacao == 1:
        print("\nsaindo...")
        print("\nSaque de R$:",limite," feito com sucesso")
    elif operacao == 2:
        print('\nObrigado pela sua atenção')
    else:
       print("Nenhuma opção foi selecionada , reinicie o sistema e digite a opção 1 ou 2")

else:
      print("\nInfelizmente esse serviço não está disponivel no momento tente mais tarde.")
    


