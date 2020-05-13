#Desafio 06. descobrir o dobro, o triplo e a raiz quadrada de um número
a = int(input("Digite um número: "))
print("{} é o dobro de {}".format ((a*2), a))
print("{} é o triplo de {}".format ((a*3), a))
#nesse caso específico a raiz quadrada é um número elevado a um meio
print("{} é a raiz quadrada de {}".format ((a ** (1/2)), a))
#printar a raiz quadrada com 2 digitos depois da vírgula
print("{:.2f} é a raiz quadrada de {}".format ((a ** (1/2)), a))
