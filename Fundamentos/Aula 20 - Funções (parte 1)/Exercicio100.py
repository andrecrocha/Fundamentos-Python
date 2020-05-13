"""Desafio 100. Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
vai sortear 5 números e colocá-los dentro da lista e a segunda vai somar todos os pares sorteados pela função anterior."""
from random import randint
from time import sleep


def sorteia(lst):
    print("==" * 20)
    print("Números sendo sorteados... ")
    for c in range(0, 5):
        n = randint(1, 20)
        print(f'{n}', end=" ")
        lst.append(n)
        sleep(0.5)
    print()
    print("Os números foram...")
    print(lst)
    print("==" * 20)

def somapar(lst):
    print("SOMADOR DE PARES")
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares foi {soma}.')


numeros = []
sorteia(numeros)
somapar(numeros)







