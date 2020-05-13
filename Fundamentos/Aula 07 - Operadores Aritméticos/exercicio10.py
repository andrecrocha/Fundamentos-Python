#Desafio 10. Conversor de moedas


din = float(input("Quantos reais você tem na carteira? R$"))
print("Com essa quantia você pode comprar U${:.2f}".format(din/4.50))
print("Com essa quantia você pode comprar Euros{:.2f}".format(din/5.20))
print("Com essa quantia você pode comprar Libras{:.2f}".format(din/6.20))


