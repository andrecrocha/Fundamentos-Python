"""Desafio 53. Crie um programa que leia uma frase qualquer e diga se ele é palíndromo."""
frase = str(input("Escreva uma frase qualquer: ")).strip().upper().replace(" ","")
print(frase)
frase_invertida = frase[::-1] # dá pra inverter usando a função de fatiamento, slice [start,stop,step], colocando nenhum
# campo no inicio e no final, e o passo como -1, ou seja, de trás pra frente"""
print("Essa frase é palíndroma? {}".format(frase == frase_invertida))
# dá pra inverter usando o laço for...