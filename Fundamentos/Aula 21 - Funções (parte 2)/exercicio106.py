"""Desafio 106. Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra "fim", o programa se encerrará. Use Cores. """
from time import sleep

def escreva(txt):
    print("=" * len(txt))
    print(txt)
    print("=" * len(txt))


while True:
    comando = input("Função ou biblioteca -> ").lower()
    if comando == "fim":
        print("\033[41;30m", end="")
        escreva("ATÉ LOGO!")
        print("\033[m")
        break
    print("\033[34;43m", end="")
    escreva(f'PROCESSANDO O MANUAL DO {comando}...')
    print("\033[m")
    sleep(0.5)
    print("\033[40m", end="")
    help(comando)
    print("\033[m")

