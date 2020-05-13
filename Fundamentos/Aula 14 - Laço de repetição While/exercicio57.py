""" Desafio 57. Faça um programa que leia o sexo de uma pessoa e só aceite 'M' ou 'F'. Peça o sexo até que a pessoa
digite um sexo válido """

sex = input("Escreva o seu sexo. Só M e F são válidos: ").upper().strip()[0]  # o zero só pega a primeira letra da palavra
while sex not in "MF":
    print("Código inválido. Tente novamente")
    sex = input("Escreva o seu sexo. Só M e F são válidos: ").upper().strip()[0] # o zero só pega a primeira letra

print("Sexo registrado com sucesso! Obrigado!")
