"""Desafio 87. Aprimore o desafio anterior mostrando. a) a soma de todos os valores pares; b) a soma de todos os valores da terceira
coluna; c) o maior valor da segundo linha"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Ele já insere os valores para não precisar usar o método .append
contpar = contter = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]:"))
        if matriz[l][c] % 2 == 0:
            contpar = contpar + matriz[l][c]
        if c == 2:
            contter = contter + matriz[l][c]

print("==" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:} ]", end=" ")
    print()
print()
print(f"A soma dos pares é {contpar}.")
print(f"A soma da terceira coluna é {contter}.")
print(f"E o maior número da segundo linha é {max(matriz[1])}.")


