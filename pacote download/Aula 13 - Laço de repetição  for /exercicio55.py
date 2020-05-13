"""Desafio 55. Desenvolva um programa que leia o peso de cinco pessoas, no final mostre qual foi
o maior e o menor peso lidos."""
pes = []
for c in range(1,6):
  pes.append(float(input("Ler um peso em kg:")))
pes_ord = sorted(pes)
print("O maior peso da lista é {} kg.".format(pes_ord[4]))
print("O menor peso da lista é {} kg.".format(pes_ord[0]))
print("Obrigado")

""" 
Outra forma de fazer:
maior = 0
menor = 0
for p in range (1,6):
  peso = float(input("Leia o peso: "))
  if peso == 1:
    maior = peso
    menor = peso
  else: 
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print("O maior peso foi de {} kg.format(maior))
print("O menor peso foi de {} kg.format(menor))