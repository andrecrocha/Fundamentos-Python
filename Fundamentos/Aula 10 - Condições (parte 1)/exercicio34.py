""" Desafio 34. Escreva um valor que pergunte o salário de um funcionário e calcule
o valor de seu aumento. Para salários de até 1250 reais, calcule um
aumento de 10%. Para os inferiores ou iguais, o aumento é de 15% """

sal = float(input("Escreva o salário do funcionário:")
if sal <= 1250.00:
  novosalario = sal + sal * 115/100
else:
  novosalario = sal + sal * 110/100
print("Seu novo é salário é de R$ {:.2f}".format(novosalario))
print(---FIM DO ALGORITMO---)