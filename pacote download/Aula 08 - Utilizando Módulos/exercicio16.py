#Desafio 16. Crie um programa que leia um numero real e mostre sua porção inteira, tem que importar a biblioteca .math

from math import trunc
num = float(input("Escreva um número real: "))
print("A parte inteira de {} é {}!".format(num, trunc(num)))