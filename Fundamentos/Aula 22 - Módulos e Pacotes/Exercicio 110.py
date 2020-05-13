"""Desafio 110. Adicione ao módulo moeda.py, um função chamada resumo(), que mostre na tela algumas informações geradas
pelas funções anteriores..."""

from ex111.utilidadesCeV import moeda

p = float(input("Digite um valor monetário: "))
moeda.resumo(p, 70, 45)

