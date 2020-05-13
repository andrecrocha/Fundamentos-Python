"""Desafio 108. Adapte o código do desafio 107, criando uma função adicional chamada moeda que consiga mostrar os valores
como um valor monetário formatado."""

from ex108 import moedas

p = float(input("Digite um valor monetário: "))
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}.')
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}.')
print(f'Aumentando 10%, temos {moedas.moeda(p)} é igual a {moedas.moeda(moedas.aumentar(p, 10))}.')
print(f'Diminuindo 30%, temos {moedas.moeda(p)} é igual a {moedas.moeda(moedas.diminuir(p, 30))}.')