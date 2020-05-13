# Aula 22 - Módulos e pacotes
from Uteis import numeros

num = int(input("Digite um número para calcular o fatorial: "))
resp = numeros.fatorial(num)
print(f'O fatorial de {num} é {resp}')
print(f'O dobro de {num} é igual a {numeros.dobro(num)}')
print(f'O triplo de {num} é igual a {numeros.triplo(num)}')

