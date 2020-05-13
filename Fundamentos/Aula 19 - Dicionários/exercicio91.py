"""Desafio 91. Crie um programa em que quatro jogadores joguem dados e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número."""

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': (randint(1, 6)), 'jogador2': (randint(1, 6)), 'jogador3': (randint(1, 6)), 'jogador4': (randint(1, 6))}
for e, v in jogo.items():
    print(f'{e} tirou o número {v}')
    sleep(1)
ranking = list() # para colocar os dados do dicionáro em ordem de acordo com o número do dado o dict se converte em uma lista
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print(' RANKING DOS JOGADORES ')
print()
for p, i in enumerate(ranking):
    print(f'O {p+1}o lugar foi {i[0]} com o resultado {i[1]}')




