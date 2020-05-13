# Exercicio 35. Condições de formar um triângulo.

print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)
a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))
if a < b+c and a > abs(b-c) and b < a+c and b > abs(a-c) and c < a+c and c > abs(b-a):
  print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO!")
else:
  print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!")