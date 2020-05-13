"""Desafio 107. Crie um módulo chamado moedas.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade(). Faça um programa que importe esse módulo e use algumas dessas funções."""

from ex107 import moedas

p = float(input("Digite um valor monetário: "))
print(f'O dobro de {p} é {moedas.dobro(p)}.')
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'Aumentando 10%, temos {p} é igual a {moedas.aumentar(p, 10)}')
print(f'Diminuindo 30%, temos {p} é igual a {moedas.diminuir(p, 30)}')





