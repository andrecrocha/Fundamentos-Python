#Desafio 32. Identificar se um ano é bissexto ou não.
from datetime import date # essa função é pra pegar as informações da máquina que o programa está rodando
ano = int(input("Escreva um ano qualquer. Coloque 0 para analisar o ano atual da máquina: "))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print("{} é ano BISSEXTO!".format(ano))
else:
  print("{} não é ano BISSEXTO!".format(ano))