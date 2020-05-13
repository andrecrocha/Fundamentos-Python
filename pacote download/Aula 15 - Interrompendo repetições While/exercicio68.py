"""Desafio 68. Faça um programa que jogue par ou ímpar com o computador. Ele só vai parar quando o usuário perder, mostrando
o total de vitórias consecutivas no final do programa."""
from random import randint

cont = soma = 0
while True:
    comp = randint(1, 10)
    num = int(input("Qual número você escolhe no PAR ou ÍMPAR? "))
    par_impar = str(input("Vocë quer Par ou Impar? [P ou I]? ")).strip().upper()[0]
    soma = comp + num
    if par_impar == "P" and soma % 2 == 0:
        cont += 1
        print(f"PARABÉNS, deu PAR, você escolheu {num} e o computador escolheu {comp}, a soma foi {soma}!")
    elif par_impar == "I" and soma % 2 == 1:
        cont += 1
        print(f"PARABÉNS, deu IMPAR, você escolheu {num} e o computador escolheu {comp}, a soma foi {soma}!")
    else:
        print(f"Vocë Perdeu. O computador escolheu {comp} e você {num} e a soma deu {soma}!")
        break

print(f"FIM DO PROGRAMA. Seu número de vitórias foi de {cont}.")



