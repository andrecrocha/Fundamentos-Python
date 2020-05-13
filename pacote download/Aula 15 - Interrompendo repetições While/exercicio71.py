"""Desafio 71. Simule um caixa eletrônico. Pergunte o valor a sacado em um número inteiro e o programa vai te dar a contagem
das notas. Considerando que o caixa possui notas de 50, 20, 10 e 1."""

print("---- CAIXA ELETRÔNICO DO ANDRÉ ----")

cont50 = cont20 = cont1 = cont10 = resto = 0

while True:
    num = int(input("Digite o valor que você quer sacar: R$ "))
    if num % 50 == 0:
        cont50 = num // 50
        break
    else:
        cont50 = num // 50
        resto = num % 50
    if resto % 20 == 0:
        cont20 = resto // 20
        break
    else:
        cont20 = resto // 20
        resto = resto % 20
    if resto == 10:
        cont10 = 1
        break
    elif resto > 10:
        cont10 = 1
        cont1 = resto - 10
        break
    else:
        cont10 = 0
        cont1 = resto
        break

print(" ")

if cont50 != 0:
    print(f"Você receberá {cont50} notas de 50 reais!")
if cont20 != 0:
    print(f"Você receberá {cont20} notas de 20 reais!")
if cont10 != 0:
    print(f"Você receberá {cont10} notas de 10 reais!")
if cont1 != 0:
    print(f"Você receberá {cont1} moedas de 1 real!")
print(" ")
print("Obrigado!")
