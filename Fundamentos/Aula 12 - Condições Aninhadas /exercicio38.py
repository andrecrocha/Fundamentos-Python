""" Desafio 38.
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
o primeiro valor é maior, o segundo valor é maior e não existe valor maior, os dois
são iguais. """
a = int(input("Escreva um primeiro número inteiro: "))
b = int(input("Escreva um segundo número inteiro: "))
if a > b:
  print("O primeiro número {} é maior que o segundo número {}.".format(a, b))
elif b > a:
  print("O segundo número {} é maior que o primeiro número {}.".format(b, a))
else:
  print("Não há números maiores, {} e {} são iguais!".format(a, b))
print("Obrigado!")