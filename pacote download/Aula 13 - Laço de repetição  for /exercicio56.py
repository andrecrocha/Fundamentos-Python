"""Desafio 56. Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final
do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos. """
from statistics import mean

count_mm20 = 0
soma_idade = 0
nomevelho = ""
idadevelho = 0

for c in range(1, 5):
    print("----- PESSOA {} -----".format(c))
    nome = str(input("Digite seu nome: ")).strip().upper()
    sexo = str(input("Escreva H se você for homem e M se você for mulher: ".format(c))).strip().upper()
    idade = int(input("Digite sua idade: "))
    soma_idade += idade
    if sexo == "M" and idade < 20:
        count_mm20 += 1
    if c == 1 and sexo == "H":
        nomevelho = nome
        idadevelho = idade
    if sexo == "H" and idade > idadevelho:
        nomevelho = nome
        idadevelho = idade

print("O número de mulheres com menos de 20 anos é {}.".format(count_mm20))
print("A média da idade das pessoas é {:.1f}".format(soma_idade / 4))
print("O mais velho se chama {} e tem {} anos.".format(nomevelho, idadevelho))

