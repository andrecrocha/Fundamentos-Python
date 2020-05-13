"""Desafio 82. Digitar vários números, analisá-los em uma lista, e separá-los em duas listas, uma de pares outro de ímpares"""

numeros = list()
while True:
    numeros.append(int(input("Digite um número: ")))
    sair = str(input("Você deseja sair? [S/N]?")).upper().strip()
    while sair not in "SN":
        sair = str(input("Código errado. Digite novamente: ")).upper().strip()
    if sair == "S":
        break

pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

numeros.sort()
pares.sort()
impares.sort()
print(f"A lista é:{numeros}")
print(f"Os números pares da lista são {pares}")
print(f"Os números ímpares da lista são {impares}")

