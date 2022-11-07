
def sacar(valor):
    saldo = 500
    saque = int(valor)
    if saque<=saldo:
            resultado = saldo-saque

            if resultado < 20:
                    print("Valor minimo para saque é de 20 reais. \n Reinicie a aplicação e tente novamente")
                
            elif resultado <= saldo:
                        print("Contando ás notas")
                        print("Total do saque R$:",resultado) 
            else:
                    print("Valor digitado de saque é maior que o saldo \n Tente novamente")

    
sacar(400)