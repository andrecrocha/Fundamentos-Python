""" Desafio 48. Faça um programa que calcule a soma entre todos os números impares que
são múltiplos de três e que se encontram no intervalo entre 1 e 500"""
soma = 0 # Essa variável é chamada de acumuladora, ela acumula os números e vai somando eles.
cont = 0 # Essa variável vai contar os números encontrados, em sua incidência.
for c in range(1,501,2):
  if c % 3 == 0:
    cont = cont + 1
    soma = soma + c
print(soma)
print (cont)