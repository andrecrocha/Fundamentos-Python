#Desafio 23. Separando digitos de um número
num = int(input("Digite um número entre 0 e 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("O número de unidades é {}".format(u))
print("O número de dezenas é {}".format(d))
print("O número de centenas é {}".format(c))
print("O número de milhares é {}".format(m))