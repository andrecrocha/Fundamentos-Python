""" Desafio 60. Faça um programa que leia um número qualquer e mostre seu fatorial """

""" Resolução utilizando o laço FOR

n1 = int(input("Digite um número para calcular seu fatorial: "))
contador = 1
for c in range(n1, 0, -1):
    print(c, end=" ")
    contador = contador * c
print("\nO fatorial de {} é igual {}.".format(n1, contador)) """

""" Resolução utilizando a bibloteca math
from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
fat = factorial(n)
print("O resultado é {}".format(fat)) """

num = int(input("Escreve um número para calcular seu fatorial: "))
c = num #criando um contador
produto = 1
while c > 0:
    print("{}".format(c), end=" ")
    print(" x " if c > 1 else " = ", end=" ")
    produto = produto * c
    c = c - 1
print(produto)
print("\nO fatorial de {} é igual a {}!".format(num, produto))










