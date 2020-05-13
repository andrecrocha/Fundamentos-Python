"""Desafio 86. Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado. Ao final
mostre a matriz na tela, com a formatação correta. """
# minha solução abaixo
"""
matriz = [[], [], []]

for c in range(0, 3):
    matriz[0].append(int(input(f"Digite um valor para [0,{c}]:")))
for c in range(0, 3):
    matriz[1].append(int(input(f"Digite um valor para [1,{c}]:")))
for c in range(0, 3):
    matriz[2].append(int(input(f"Digite um valor para [2,{c}]:")))
print("==" * 30)
for n in matriz[0]:
    print(f"[ {n} ]", end=" ")
print()
for f in matriz[1]:
    print(f"[ {f} ]", end=" ")
print()
for h in matriz[2]:
    print(f"[ {h} ]", end=" ")
"""
#Solução alternativa, dada pela video aula
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Ele já insere os valores para não precisar usar o método .append
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]:"))
print("==" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:} ]", end=" ")
    print()





