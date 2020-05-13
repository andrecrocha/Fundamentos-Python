"""Desafio 54. Crie um programa que leia a idade de sete pessoas, e diga quantas já são
maior de idade e quantas ainda não atingiram a maior idade"""
count_ma = 0
count_me = 0
for i in range(1,8):
  idade = int(input("Digite a idade da pessoa {}: ".format(i)))
  if idade >= 21:
    count_ma += 1
  else:
    count_me += 1
print("O número de pessoas maiores de idade é {} e menores é {}!".format(count_ma, count_me))