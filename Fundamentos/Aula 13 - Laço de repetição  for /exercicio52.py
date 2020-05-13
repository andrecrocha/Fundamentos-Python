"""Desafio 52. Faça um programa que leia um número inteiro e diga se ele é o não um
número primo."""

num = int(input("Digite um número inteiro: ")) #entrada do número inteiro
tot = 0 #contador do número de divisores do número
for c in range(1, num+1):
  if num % c == 0:
    print("\033[33m", end=" ")
    tot += 1
  else:
    print("\033[31m", end=" ")
  print("{}".format(c), end=" ")
print("\n\033[36mO número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
  print("\033[37mPor isso ele É PRIMO!")
else:
  print("\033[35mPor isso ele NÃO É PRIMO!")