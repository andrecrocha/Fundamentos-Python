#Exercicio 33. Ler três valores. E mostrar o maior e o menor.
n1 = float(input("Digite um primeiro número: "))
n2 = float(input("Digite um segundo número: "))
n3 = float(input("Digite um terceiro número: "))
numeros = [n1, n2, n3] # criar uma lista
numeros_ordenados = sorted(numeros) # usar a função sorted pra ordenar a lisa do maior pro menor
print("O maior número é {}.".format(numeros_ordenados[2]))
print("O menor número é {}.".format(numeros_ordenados[0]))
print("Obrigado")