""" Desafio 17. Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
e mostre o comprimento da hipotenusa."""

from math import sqrt, pow, hypot
catop = float(input("Escreva o comprimento do cateto oposto: cm "))
catad = float(input("Escreva o comprimento do cateto adjacente: cm "))
hip = sqrt(pow(catop, 2) + pow(catad, 2))
print("A hipotenusa é igual a {:.2f}".format(hip))
#ou pode-se usar a função math.hypot
print(math.hypot(catop, catad))