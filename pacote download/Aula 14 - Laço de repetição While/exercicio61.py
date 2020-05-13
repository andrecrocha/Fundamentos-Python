"""Desafio 61. Refaça o desafio 51 utilizando a estrutura de repetição while. Leia o primeiro 
termo e a razão de uma PA e mostre os 10 primeiros termos da progressão usando a estrutura while."""

i = int(input("O primeiro termo da PA é: "))
r = int(input("A razão da PA é: "))
decimo1 = i + (11 - 1) * r
c = i

print("Os dez primeiros termos da PA são:")
while c != decimo1:
    print("{}".format(c), end=" ")
    c = c + r
print("\nFIM")