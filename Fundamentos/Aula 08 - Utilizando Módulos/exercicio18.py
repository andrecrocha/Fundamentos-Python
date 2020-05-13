#Desafio 18. Dar o seno, cosseno e tangente de um ângulo
import math
ang = float(input("Escreva o valor de um ângulo: "))
#Só que, de acordo com a biblioteca, temos que converter o ângulo primeiro para radianos
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print("O seno de {} é igual a {:.2f}".format(ang, seno))
print("O cosseno de {} é igual a {:.2f}".format(ang, cos))
print("A tangente de {} é igual a {:.2f}".format(ang,tang))