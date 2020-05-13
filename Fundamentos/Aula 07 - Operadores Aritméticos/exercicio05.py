#Desafio 05. Dê o sucessor e o antecessor de um número e imprima "analisando esse número seu
#sucessor é x e seu antecessor é y"

a = int(input("Digite um número inteiro: "))
suc = a+1
ant = a-1
print("Analisando {}, seu sucessor é {} e seu antecessor é {}".format(a, suc, ant))