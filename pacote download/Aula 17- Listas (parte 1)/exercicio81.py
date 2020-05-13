"""Desafio 81. Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre; a) Quantos números
foram digitados; b) A lista de valores ordenada de forma decrescente; c) se o valor 5 está ou não na lista."""

numeros = []
while True:
    numeros.append(int(input("Escreva um valor inteiro: ")))
    sair = str(input("Você deseja sair? [S/N]")).upper().strip()
    while sair not in "SN":
        sair = str(input("Código inválido. Digite novamente: ")).upper().strip()
    if sair == "S":
        break

print(" ")
print(f"Foram {len(numeros)} números digitados.")
numeros.sort(reverse=True)
print(f"A lista em ordem descrescente é: {numeros}.")
print(f"O valor 5 está na lista? {5 in numeros}")
print("Obrigado!")

