""" Exercicio 27: Faça um programa que leia o nome completo de uma pessoa mostrando em
seguida o primeiro e o último nome separadamente
"""
nome = str(input("Escreva o seu nome: ")).strip()
divid = nome.split()
print("Analisando o seu primeiro nome...")
print("Seu primeiro nome é {}.".format(divid[0]))
#revertendo a sequência da lista e lendo o último nome
divid.reverse()
print("Seu último nome é {}.".format(divid[0]))
# Essa última, de ler o último nome, pode ser feito de outra forma... por exemplo,
# print(divid(len(divid)-1)).. ou seja, a posição da último elemento a partir da número de elementos da lista...