""" Desafio 39. Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
- Se ele ainda vai se alistar
- Se ele tem que se alistar
- Se ele já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """

from datetime import date
sexo = str(input("Olá diga se você é homem ou se você é mulher: ")).strip().upper()
if sexo == "MULHER":
  print("Você não precisa se alistar, tenha um bom dia!")
else:
  nasc = int(input("Olá jovem, em que ano você nasceu? "))
  ano_atual = date.today().year
  idade = ano_atual - nasc
  if idade == 18:
    print("Você terá que se alistar esse ano, fique atento!")
  elif idade > 18:
    print("Já passou da hora de se alistar, você passou {} anos do prazo!".format(idade - 18))
    print("Seu alistamento foi em {}!".format(ano_atual - (idade-18)))
  else:
    print("Você ainda não poderá se alistar, só em {}!".format(18 - idade + ano_atual))
  print("Obrigado!")