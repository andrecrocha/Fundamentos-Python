""" Desafio 26. Faça um programa que leia uma frase pelo teclado e mostre:
a) Quantas vezes aparece a letra "a"
b) Em que posição ela aparece a primeira vez
c) Em que posição ela aparece a última vez
"""
# letra a)
frase = str(input('Escreva uma frase:')).strip().upper()
print(frase.count('A'))
# letra b)
print(frase.find('A')+1)
# letra c)
print(frase.rfind("A")+1)