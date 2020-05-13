"""Desafio 99. Faça um programa que receba vários parâmetros com valores inteiros seja capaz de analisar todos os valores
e dizer qual é o maior. """
from time import sleep

def maior(* num):
    print("==" * 5, "ANALISANDO OS VALORES PASSADOS", "==" * 5)
    for c in num:
        print(f'{c}', end=" ")
        sleep(0.5)
    print(f'\nForam analisados {len(num)} valores.')
    print(f'E o maior valor é {max(num)}')


maior(5, 6, 7, 8)
maior(5, 1, 3, 3, 2, 5, 10)
maior(3, 2)

