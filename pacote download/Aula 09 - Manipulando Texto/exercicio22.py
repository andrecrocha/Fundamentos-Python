"""Desafio 22. Crie um programa que leia o nome completo de uma pessoa, e mostre
a)O nome com todas as letras maiusculas
b)O nome com todas as minúsculas
c)Quantas letras ao todo, sem considerar espaços
d)Quantas letras tem o primeiro nome
"""
nome = str(input('Escreva seu nome todo: ')).strip()
# letra a -> o nome com todas as maiúsculas
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}.".format(nome.upper()))
# letra b -> o nome com todas as minúsculas
print("Seu nome em minúsculas é {}.".format(nome.lower()))
# letra c -> quantas letras ao todo sem considerar espaços
# Você vai fazer esse exercício dando lenght primeiro e depois tirando o numero de vezes que tem espaço ' '
print("Seu nome tem {} letras".format(len(nome) - nome.count(' ')))
# letra d -> quantas letras tem o primeiro nome. Tem duas maneiras de fazer isso
# A primeira é tentando achar a posição do primeiro espaço, e aí o Python vai contar o número de caracteres até ele
print("Seu primeiro nome tem {} letras.".format(nome.find(" ")))
# A segunda é fazendo uma lista, e depois contando o número de caracteres dentro do primeiro elemento da lista
lista = nome.split()
print("Seu primeiro nome tem {} letras.".format(len(lista[0])))