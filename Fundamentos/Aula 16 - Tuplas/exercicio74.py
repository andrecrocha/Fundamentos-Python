""" Desafio 74. Gerar 5 numeros aleatórios. Colocar numa tupla. Mostrar o maior e o menos valores"""
from random import randint
a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)
tupla = (a, b, c, d, e)
print(f"Os números sorteados foram {tupla}.")
print(f"O maior valor é {sorted(tupla)[-1]}.") # pode ser usada a função max(tupla)
print(f"O menor valor é {sorted(tupla)[0]}.") #pode ser usada a função min(tupla)




