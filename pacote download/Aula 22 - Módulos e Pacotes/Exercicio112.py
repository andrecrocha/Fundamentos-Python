"""Desafio 112. No módulo dados, crie um validador de dados, que leia só números monetários. """

from ex111.utilidadesCeV import dado, moeda

p = dado.leiadinheiro("Digite um valor monetário: ")
moeda.resumo(p, 20, 40)

