"""Desafio 103. Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido informado coretamente."""

def ficha(gols = 0, nome = ""):
    if nome == "":
        nome = "<desconhecido>"
    return f'O jogador {nome} marcou {gols} gols!'

nome = input("Qual é o nome do jogador: ").strip()
gols = input("Quantos gols o jogador marcou: ").strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(ficha(gols, nome))

print(ficha(5, "Pedro"))





