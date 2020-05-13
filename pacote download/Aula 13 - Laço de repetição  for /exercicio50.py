"""Desafio 50. Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o"""
soma = 0
impar = 0
for cont in range(1,7):
  n = int(input("Escreva um número inteiro: "))
  if n % 2 == 0:
    soma = soma + n
  else:
    impar = impar + n
print("A soma só dos números pares é {} e dos impares é {}!".format(soma, impar))