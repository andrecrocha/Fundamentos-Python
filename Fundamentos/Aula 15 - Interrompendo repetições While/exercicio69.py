""" Desafio 69. Programa que leia idade e sexo de pessoas. A cada digitação pergunte se o usuário quer ou não continuar.
 No final mostre o a) quantas pessoas tem mais de 18 anos; b) quantos homens foram cadastrados; c) quantas mulheres tem
 menos de 20 anos. """

mais18 = homens = mulheresm20 = 0

while True:
    idade = int(input("Qual sua idade? "))
    sexo = str(input("Qual seu sexo? [M / F]")).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input("Qual seu sexo? [M / F]")).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheresm20 += 1
    continuar = str(input("Você quer continuar? [S / N]")).strip().upper()
    while continuar not in "SN":
        continuar = str(input("Você quer continuar? [S / N]")).strip().upper()
    if continuar == "N":
        break
print(" ")
print(f"{mais18} pessoas tem mais de 18 anos!")
print(f"{homens} homens foram cadastrados!")
print(f"{mulheresm20} mulheres tem menos de 20 anos!")
print("Obrigado!")



