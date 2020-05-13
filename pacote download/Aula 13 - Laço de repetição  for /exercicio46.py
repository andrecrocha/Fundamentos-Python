""" Laços de repetição. FOR
Desafio 46. Faça um programa que mostre na tela uma contagem regressiva de 10 até
0, com uma pausa de 1 segundo entre eles. """
from time import sleep
print("{:=^40}".format(" CONTAGEM REGRESSIVA "))
for c in range (10, -1, -1):
  print(c)
  sleep(1)
print("Estourou os fogos!!!")