""" Exercico 29: Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada kilômetro acima
do limite de velocidade
"""
vel = float(input("Escreva a velocidade do carro em km: "))
if vel >80:
  print("Infelizmente você foi multado!")
  multa = (vel-80) * 7
  print("O valor da sua multa foi de R$ {:.2f}.".format(multa))
else:
  print("Parabéns, você não foi multado!")
print("Obrigado!")