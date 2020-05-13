"""Desafio 109. Modifique as funções que foram criadas no desafio 107 para que eles aceitem um parâmetro a mais,
informando se o valor retornado por eles vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108"""

from ex108 import moedas

p = float(input("Digite um valor monetário: "))
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}.')
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}.')
print(f'Aumentando 10%, temos {moedas.moeda(p)} é igual a {moedas.aumentar(p, 10, True)}.')
print(f'Diminuindo 30%, temos {moedas.moeda(p)} é igual a {moedas.diminuir(p, 30, True)}.')