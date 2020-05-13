""" Desafio 49. Refazer o exercicio da tabuada utilizando o laço for."""
print("{:=^40}".format(" TABUADA DO ANDRÉ "))
n = int(input("Escreve um número inteiro e faremos a tabuada para você: "))
for c in range(0,11):
  print("{} x {} é igual a {}!".format(n, c, (n*c)))
print("Obrigado!")