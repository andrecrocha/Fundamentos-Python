# listas são mutáveis ao contrário das tuplas, que são imutáveis.
numeros = [3, 4, 6, 7, 9]
print(numeros)
numeros[3] = 10 #trocar um elemento. O elemento 3 passa a ser o elemento 10.
print(numeros)
numeros.append(4) #adiciona um elemento ao final da lista
print(numeros)
numeros.insert(2, 8) #Adicionar o elemento 8 na posição 2... o resto vai pra frente
print(numeros)
numeros.sort() #ordenar a lista do menor para o maior
print(numeros)
numeros.sort(reverse=True) # ordenar de modo inverso
print(numeros)
numeros.pop() #remove o último valor da lista
print(numeros)
numeros.pop(2) #remove o valor na posição indicada
print(numeros)
numeros.remove(4) #remove o valor indicado, se tiver dois ele remove o primeiro
print(numeros)
# uma outra maneira de visualizar a lista é com o laço for
for v in numeros:
    print(f"{v}", end=" ")
# mostrar os valores com suas posições
print(" ")
for c, v in enumerate(numeros):
    print(f"O valor {v} está na posição {c}.")
# eu posso também ler valores e colocar dentro de uma lista
valores = list()
for cont in range(0,5):
    valores.append(int(input("Digite um valor:")))
print(" ")
print(valores)
# no pyhton você pode criar duas listas e igualar uma a outra... mas isso não copia a lista, elas se igualam na memória
# e se uma for alterada a outra será alterada.
a = [1, 3, 5, 7]
b = a
print(a)
print(b)
# para fazer cópia o comando teria que ser -> b = a[:]

