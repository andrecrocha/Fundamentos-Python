""" Desafio 42. Cria um programa que leia os segmentos, veja se é possível criar um
triângulo, e diga que tipo de TRiÂNGULO é possível fazer. Equilátero:todos os lados iguais,
Escaleno:todos os lados diferentes, Isósceles:dois lados iguais """
print("-=-" * 20)
print("Analisador de triângulos e seu tipo")
print("-=-" * 20)
a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))
if a < b+c and a > abs(b-c) and b < a+c and b > abs(a-c) and c < a+c and c > abs(b-a):
  if a == b == c:
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO e ele é EQUILÁTERO!")
  elif a != b != c !=a: #tomar muito cuidado aqui, pq a!=b!=c não é suficiente, pois o python pode ler um isósceles como escaleno
     print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO e ele é ESCALENO!")
  else:
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO e ele é ISÓSCELES!")
else:
  print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!")
print("Obrigado!")