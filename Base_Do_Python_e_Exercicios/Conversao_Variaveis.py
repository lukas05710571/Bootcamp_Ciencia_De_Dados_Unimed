
Pedidos = [["Produto"],["Valor_Do_Produto"]]
Lista_Produto = Pedidos
Lista_Produto[0][0] = "Escova de dente"
Lista_Produto[1][0] = 10.90

Produto =str(Lista_Produto[0][0])
Valor_Produto = str(Lista_Produto[1][0])

print(f"\nProduto : {Produto} \nValor Do Produto : {Valor_Produto}")
# print("Pedido n° 5 : \n Produto : \n",Lista_Produto[0][0],"Valor a pagar: \n",Lista_Produto[1][0])