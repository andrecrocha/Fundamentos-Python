"""Desafio 51. Contar os 10 primeiros termos de uma Progressão Aritmética! """
i = int(input("Digite o inicio da PA: "))
r = int(input("Digite a razão da PA: "))
decimo = i + (11-1)* r
for c in range(i, decimo, r):
  print(c)