""" Desafio 98. Faça um programa que tenha uma função chamada contador, que receba três parâmetros fixos, inicio, fim e
passo. Seu programa tem que realizar três contagens... a) de 1 até 10, de 1 em 1; b) de 10 até 0, de 2 em 2; c) uma contagem
personalizada; c) uma contagem personalizada"""
from time import  sleep

def contador(inicio, fim, it):
    print("==" * 20)
    print(f'Contando de {inicio} até {fim}, de {abs(it)} em {abs(it)}')
    if it == 0:
        it = 1
    if inicio > fim and it > 0:
        it = -1 * it
        for c in range(inicio, fim - 1, it):
            print(f'{c}', end= " ")
            sleep(0.5)
    elif inicio < fim:
        for c in range(inicio, fim + 1, it):
            print(f'{c}', end= " ")
            sleep(0.5)
    elif inicio > fim:
        for c in range(inicio, fim - 1, it):
            print(f'{c}', end= " ")
            sleep(0.5)
    print()
    print("==" * 20)

#Programa principal

contador(1, 10, 1)
contador(10, 0, -2)
contador(10, 5, 1)
print("Agora é a sua vez de definir a contagem")
a = int(input("Inicio: "))
b = int(input("Fim: "))
c = int(input("Passo: "))
contador(a, b, c)

