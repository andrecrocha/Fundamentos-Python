""" Crie um programa que leia vários números inteiros. O programa só para quando o usuário digitar 999. Mostre quantos
números foram digitados e qual foi a soma entre eles desconsiderando o flag (999) """

num = cont = somatorio = 0
num = int(input("Escreva um número inteiro: ")) #nesse caso você coloca uma leitura fora do laço e uma na última posição do laço
while num != 999:
    cont += 1
    somatorio = somatorio + num
    num = int(input("Escreva um número inteiro: ")) #para eliminar a contagem e a soma do "flag", isto é, o número de saída

print("O número de números digitados foi {} e a soma entre eles foi {}.".format(cont , somatorio))
