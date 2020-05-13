""" Estruturas aninhadas.
Desafios. Desafio 36.
Escreva um programa para aprovar um empréstimo bancário de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador, e em quantos anos ele vai pagar. Calcule o valor mensal da prestação, sabendo que ela
não vai exceder 30% do salário ou então o empréstimo será negado."""
val = float(input("Escreva o valor da casa: R$"))
sal = float(input("Escreva o seu salário: R$"))
ano = int(input("Escreva em quantos anos você quer pagar o empréstimo: "))
val_mensal = val / (ano*12)
if val_mensal <= sal * 30 / 100:
  print("Parabéns seu empréstimo foi aprovado. O valor mensal da prestação será de R$ {:.2f}!".format(val_mensal))
else:
  print("Infelizmente seu empréstimo foi negado!")
print("Obrigado!")