#Desafio 12. Calculando um desconto de 5% no preço de um produto
preco = float(input("Qual é o preço do seu produto: R$ "))
desc = preco - preco * 5/100
print("A sua compra de R$ {} com um desconto de 5% sai no valor de R$ {:.2f}".format(preco, desc))