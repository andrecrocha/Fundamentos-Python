"""Deafio 70. Faça um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
quer continuar. No final mostre a) o total gasto na compra; b) quantos produtos custam mais de 1000 reais; c) Qual o nome
do produto mais barato."""

total = mais1000 = cont = precobarato = 0
barato = " "

print("{:=^40}".format(" LOJAS ANDRÉ "))
while True:
    preco = float(input("Digite o valor do produto: R$ "))
    nome = str(input("Qual é o nome do produto? ")).strip().capitalize()
    total += preco
    cont += 1
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        precobarato = preco
        barato = nome
    else:
        if preco < precobarato:
            barato = nome
    continuar = str(input("Quer continuar? [S/N]?")).strip().upper()
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]?")).strip().upper()
    if continuar == "N":
        break

print(" ")
print(f"\033[1;32mO total das compras foi no valor de R$ {total:.2f}.\033[m")

print(f"\033[1;34mForam {mais1000} produtos que custaram mais de 1000 reais.\033[m")

print(f"\033[1;35mO produto mais barato foi {barato}.\033[m")
print(" ")
print("\033[1;36mObrigado pela preferência!\033[m")


