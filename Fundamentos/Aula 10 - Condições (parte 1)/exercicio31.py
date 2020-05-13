"""#Exercicio 31. Crie um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando 0,50 por Km para viagens de até 200 km e
e 0,45 R$ para viagens mais longas """
dist = float(input("Escreva a distância da viagem em km: "))
if dist <= 200.00:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print("O preço da sua passagem é de R$ {:.2f}!".format(preco))

print("Obrigado!")