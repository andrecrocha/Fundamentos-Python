"""Desafio 76. Listagem de preços. """

compras = ("Pão", 2.30, "Manteiga", 5.70, "Leite", 9.60, "Arroz", 5.70, "Shampoo", 15.60)
print("**" * 20)
print("Listagem de compras")
print("**" * 20)

for pos, e in enumerate(compras):
    if pos % 2 == 0:
        print(f"{compras[pos]}................. R$ {compras[pos+1]:.2f}")
print(" ")
print("**" * 20)
print("Obrigado!")


