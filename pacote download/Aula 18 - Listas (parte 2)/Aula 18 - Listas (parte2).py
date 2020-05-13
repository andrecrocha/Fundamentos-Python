# Listas dentro de listas

"""
l = [[4, 2, 6, 8], [3, 5, 9, 1]]
for num in l[0]:
    print(num) """

# colocar uma lista dentro da outra
lista1 = [1, 4, 5, 7]
lista2 = ["Maria", "João", "Paulo", "Vanessa"]
# vamos colocar todos esses elementos na lista3
lista3 = [[54.5, 34.6, 87.4, 35]]
lista3.append(lista1[:]) # você está fazendo uma cópia da lista1 e jogando dentro da lista 3
print(lista3)
lista3.append(lista2[:])
print(lista3)


