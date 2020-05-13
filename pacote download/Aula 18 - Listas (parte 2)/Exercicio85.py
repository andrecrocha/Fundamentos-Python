""""Desafio 85. Faça um programa em que um usuário digite sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os pares e os ímpares. No final mostre os pares e os ímpares em ordem crescente. """

numeros = [[], []]
valor = 0

for num in range(1, 8):
    valor = int(input(f"Digite o {num}o número da lista: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print()
print(f"O conjunto dos números foi: {numeros}")
numeros[0].sort()
print(f"O conjunto dos pares foi: {numeros[0]}")
numeros[1].sort()
print(f"O conjunto dos impares foi: {numeros[1]}")










