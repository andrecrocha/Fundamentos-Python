"""Desafio 93. Rendimento de um jogador. Anotar nome e quantas partidas jogou. Depois perguntar quantos gols ele fez
em cada partida... """

jogador = {}
scores = []
jogador["nome"] = str(input("Qual é o nome do jogador? ")).strip()
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, n):
    num = int(input(f"Qual gols ele fez na partida {c+1}? "))
    scores.append(num)

jogador["gols"] = scores[:]
jogador["total"] = sum(scores) # o método sum() soma os valores dentro de uma lista
print("==" * 30)
print(jogador)
print("=="* 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print("===" * 30)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
for pos, c in enumerate(jogador["gols"]):
    print(f'   => No jogo {pos+1}, o jogador fez {c} gols')
print(f'O total de gols foi {jogador["total"]}')

