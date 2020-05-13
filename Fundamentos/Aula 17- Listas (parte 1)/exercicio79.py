"""Desafio 79. Faça um programa que leia inúmeros valores e os coloque numa lista. Se o número já tiver sido adicionado
não o coloque na lista. Ao final de cada número digitado será perguntado se o usuário quer sair do programa. Ao final mostre
os números da lista em ordem crescente."""

val = list()
while True:
    num = int(input("Digite um valor: "))
    if num not in val:
        val.append(num)
    else:
        print(f"{num} já está na lista, não foi adicionado...")

    sair = str(input("Você deseja sair? [S/N]?")).upper().strip()
    while sair not in "SN":
        sair = str(input("Digitou errado. Você deseja sair? [S/N]?")).upper().strip()
    if sair == "S":
        break

val.sort()
print(val)


