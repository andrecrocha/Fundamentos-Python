"""Desafio 84. Faça um programa que leia nome e peso de várias pessoas e coloque tudo dentro de uma lista. Ao final mostre
a) quantas pessoas foram cadastradas; b) uma listagem com as pessoas mais pesadas; c) uma listagem com as pessoas mais leves"""

pessoas = list()
galera = list()
maior = list()
menor = list()

while True:
    pessoas.append(str(input("Escreve o nome: ")))
    pessoas.append(float(input("Digite seu peso: ")))
    galera.append(pessoas[:])
    pessoas.clear()
    sair = str(input("Você quer sair? [S / N]?")).strip().upper()
    while sair not in "SN":
        sair = str(input("Código errado. Digite novamente: ")).strip().upper()
    if sair == "S":
        break

for pos, c in enumerate(galera):
    if pos == 0:
        maior.append(c)
        menor.append(c)
    else:
        if c[1] > maior[0][1]:
            maior.clear()
            maior.append(c)
        elif c[1] == maior[0][1]:
            maior.append(c)
        elif c[1] < menor[0][1]:
            menor.clear()
            menor.append(c)
        elif c[1] == menor[0][1]:
            menor.append(c)

print("As pessoas mais pesadas foram:{}".format(""), end=" ")
for p in maior:
    print(f"[{p[0]}]", end=" ")
print("\nAs pessoas mais leves foram:{}".format(""), end=" ")
for v in menor:
    print(f"[{v[0]}]", end=" ")

print(f"\nO número de pessoas contadas foi {len(galera)}")

















