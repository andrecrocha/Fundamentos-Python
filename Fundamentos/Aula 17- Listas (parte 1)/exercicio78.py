"""Desafio 78. Digite 5 valores númericos e coloque-os numa lista. No final mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista."""

valores = list()
for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
print(" ")

print(f"O maior valor foi {max(valores)} e sua posição na lista foi {valores.index(max(valores)) + 1}")

print(f"O menor valor foi {min(valores)} e sua posição na lista foi {valores.index(min(valores)) + 1}")




