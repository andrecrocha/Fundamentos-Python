"""Desafio 111. Crie um pacote chamado utilidadeCev que tenha dois módulos internos, chamados moeda e
dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109, para o primeiro pacote e mantenha
tudo funcionando..."""

from ex111.utilidadesCeV import moeda

p = float(input("Digite um número: "))
moeda.resumo(p, 45, 20)

