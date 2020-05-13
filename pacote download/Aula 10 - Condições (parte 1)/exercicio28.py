""" Exercício de condições simples e compostas
Exercício 28: Faça um programa que faça o computador pensar um número inteiro entre 0 e 5 e peça
para o usuário descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
na tela se o usuário perdeu ou venceu! """
import random
from time import sleep
print("-=-" * 20)
n = int(input("Escreve um número na tela de 1 a 5: "))
sort = random.randrange(1,6)
print("PROCESSANDO...")
sleep(3) # Da biblioteca 'time' importamos a função sleep, em que o computador espera antes de realizar a função. Neste caso ele espera 3 segundos
print("O número sorteado foi {}.".format(sort))
if n == sort:
  print("PARABÉNS VOCÊ VENCEU!!")
else:
  print("Infelizmente você perdeu, tente novamente!")
print("Obrigado o André, agradece!")
print("-=-" * 20)