""" Desafio 43. Calcule o IMC de uma pessoa e mostre seu status, de acordo com a tabela:
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida
"""
print("=+=" * 25)
print("Calculadora de IMC")
print("=+=" * 25)
altura = float(input("Diga sua altura: "))
peso = float(input("Diga seu peso: "))
imc = peso / (altura ** 2)
if imc < 18.5:
  print("Seu IMC é de {:.2f} e você está ABAIXO DO PESO!".format(imc))
elif imc >= 18.5 and imc < 25:
  print("Seu IMC é de {:.2f} e você está no PESO IDEAL!".format(imc))
elif imc >= 25 and imc < 30:
  print("Seu IMC é de {:.2f} e você está com SOBREPESO!".format(imc))
elif imc >= 30 and imc < 40:
  print("Seu IMC é de {:.2f} e você está com OBESIDADE!".format(imc))
else:
  print("Seu IMC é de {:.2f} e você está com OBESIDADE MÓRBIDA!".format(imc))
print("Obrigado!")