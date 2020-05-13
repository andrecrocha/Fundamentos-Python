""" Desafio 41. A confederação nacional de natação quer um programa que saiba a idade e a
categoria de um jovem. Sendo até 9anos Mirim, até 14 anos Infantil, até 19 anos Junior
e até 20 anos Sênior. Acima disso Master!"""
idade = int(input("Qual é sua idade?: "))
if idade <= 9:
  print("Sua categoria é MIRIM!")
elif idade <= 14:
  print("Sua categoria é INFANTIL!")
elif idade <= 19:
  print("Sua categoria é JÚNIOR!")
elif idade <= 25:
  print("Sua categoria é SÊNIOR!")
else:
  print("Sua categoria é MASTER!")
print("Valeu!")