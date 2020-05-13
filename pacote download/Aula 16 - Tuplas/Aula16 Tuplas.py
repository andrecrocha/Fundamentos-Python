lanche = "Hamburguer", "Pizza", "Suco", "Pudim"
# print(lanche[-3:])

# utilizações do FOR com tuplas
# para imprimir os elementos

# for comida in lanche:
#   print(f"Eu vou comer {comida}.")

# para imprimir os elmentos e suas posições. Opção 1:
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}.")

# Ou:
# for pos, comida in enumerate(lanche):
#    print(f"Eu vou comer {comida} na posição {pos}.")

# ele não muda a tupla, mas coloca em ordem com o método sorted()
print(sorted(lanche))

# eu posso unir duas tuplas
a = (1, 4, 6, 9)
b = (9, 3, 4)
c = a + b
print(c)
print(c.count(9)) # quantas vezes aparece o 9 na tupla
print(c.index(1)) # me mostra a posição do elemento
print(c.index(9)) #se tiver duas ocorrências ele pega a primeira
print(c.index(9, 4)) #agora a partir da quarta posição
# No Python também é possível ter dados de difentes tipos dentro da mesma tupla
pessoa = ("André", 27, "Belo Horizonte", 55)
print(pessoa)
# a tupla é imutável a não ser para ser deletada por inteiro, não um elemento só
# para isso se usa o método: del("nome da tupla")



