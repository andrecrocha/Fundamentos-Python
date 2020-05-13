"""Desafio 95. Aprimore o 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de
aproveitamento de cada jogador."""

jogador = {}
scores = []
lista = []
tot = 0
while True:
    jogador.clear()
    print("==" * 30)
    jogador["nome"] = str(input("Qual é o nome do jogador? ")).strip()
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, n):
        num = int(input(f"Qual gols ele fez na partida {c+1}? "))
        tot += num
        scores.append(num)
    jogador["gols"] = scores[:]
    scores.clear()
    jogador["total"] = tot
    tot = 0
    lista.append(jogador.copy())
    sair = input("Você deseja sair? [S/N]").strip().upper()
    while sair not in "SN":
        sair = input("Código incorreto. Digite novamente: ").strip().upper()
    if sair == "S":
        break

print("=" * 30, " ANALISADOR DE DESEMPENHO ", "=" * 30)
print("código", end=" ")
for i in jogador.keys():
    print(f'{i:<12}', end=" ")
print()
for k, v in enumerate(lista):
    print(f'{k:>2}', end=" ")
    for d in v.values():
        print(f'{str(d):<15}', end= " ")
    print()
print("==" * 30)

while True:
    n1 = int(input("De qual jogador você quer ver o desempenho individual? (999 para parar)"))
    while n1 >= len(lista) and n1 != 999:
        n1 = int(input("Código errado. Digite novamente: "))
    if n1 == 999:
        break
    else:
        print(f'LEVANTAMENTO DO JOGADOR {lista[n1]["nome"]}')
        for p, v in enumerate(lista[n1]["gols"]):
            print(f' ==> No jogo {p+1}, ele fez {v} gols')

print()
print("<<< VOLTE SEMPRE >>>")




