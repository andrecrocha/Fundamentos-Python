"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de
Fibonacci ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8..."""

print("Sequência de Fibonacci")
print("+=+" * 20)

n = int(input("Quantos números da sequência você quer ler? "))
cont = soma = 0
t1 = 0
t2 = 1
print("{} {}".format(t1, t2), end=" ")
cont = 3
while cont <= n:
    soma = t1 + t2
    t1 = t2
    t2 = soma
    cont += 1
    print(soma, end=" ")


