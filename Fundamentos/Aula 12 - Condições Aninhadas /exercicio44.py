""" Desafio 44. Elabore um programa que calcule o valor a ser pago por um produto, considerando
seu preço normal e condição de pagamento:
- a vista no dinheiro/cheque: 10% de desconto
- a vista no cartão de desconto: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros """

print("{:=^40}".format(" LOJAS ANDRÉ "))
preco = float(input("Qual é o valor do produto? "))
cond = int(input("""Qual é a condição de pagamento? Aqui são as opções:
Digite 0: À vista no dinheiro ou cheque você tem 10% de desconto.
Digite 1: À vista no cartão de desconto você tem 5% de desconto.
Digite 2: Em até 2x no cartão o preço é normal.
Digite 3: 3x ou mais no cartão você terá 20% de juros
"""))
if cond == 0:
  print("De acordo com a opção de pagamento seu produto custará R$ {:.2f}.".format(preco - preco * 10/100))
elif cond == 1:
  print("De acordo com a opção de pagamento seu produto custará R$ {:.2f}.".format(preco - preco * 5/100))
elif cond == 2:
  print("De acordo com a opção de pagamento seu produto custará R$ {:.2f}.".format(preco))
elif cond == 3:
  print("De acordo com a opção de pagamento seu produto custará R$ {:.2f}.".format(preco + preco * 20/100))
else:
  print("Opção de compra inválida! Tente novamente")
print("Obrigado!")