"""Desafio 80. Ler cinco valores númericos e ir colocando eles na lista de modo ordenado sem usar o método sort"""

numeros = list()
for cont in range(0, 5):
    num = int(input("Escreva um número: "))
    if cont == 0:
        numeros.append(num)
    elif cont == 1:
        if num >= numeros[0]:
            numeros.append(num)
        else:
            numeros.insert(0, num)
    elif cont == 2:
        if num >= numeros[1]:
            numeros.append(num)
        elif num <= numeros[0]:
            numeros.insert(0, num)
        else:
            numeros.insert(1, num)
    elif cont == 3:
        if num >= numeros[2]:
            numeros.append(num)
        elif num <= numeros[0]:
            numeros.insert(0, num)
        elif num > numeros[0] and num <= numeros[1]:
            numeros.insert(1, num)
        else:
            numeros.insert(2, num)
    elif cont == 4:
        if num >= numeros[3]:
            numeros.append(num)
        elif num <= numeros[0]:
            numeros.insert(0, num)
        elif num > numeros[0] and num <= numeros[1]:
            numeros.insert(1, num)
        elif num > numeros[1] and num <= numeros[2]:
            numeros.insert(2, num)
        else:
            numeros.insert(3, num)





print(numeros)


