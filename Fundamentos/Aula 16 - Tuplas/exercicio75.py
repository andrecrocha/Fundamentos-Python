""" Desafio 75. Faça um programa que peça 4 valores pelo teclado e guarde-os em uma tupla. No final mostre. a)quantas
vezes apareceu o valor 9; b) em que posição foi digitado o primeiro valor 3; c) quais foram os pares."""


tupla = (int(input("Digite um valor: ")),
         int(input("Digite um outro valor: ")),
         int(input("Digite um terceiro valor: ")),
         int(input("Digite um quarto valor: ")))
print(tupla)
print(f"O valor 9 apareceu {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"O valor 3 apareceu pela primeira vez na {tupla.index(3) + 1}a posição.")
else:
    print("O valor 3 não apareceu nenhuma vez.")
print("Os números pares da tupla foram esses:", end=" ")
for num in tupla:
    if num % 2 == 0:
        print(f"{num}", end=" ")





