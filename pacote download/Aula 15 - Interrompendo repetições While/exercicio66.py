""" Desafio 66. Crie um programa que leia vários números inteiros, o 999 é para parar. Calcule a soma sem o flag, isto é
o 999"""

soma = cont = 0

while True:
    num = int(input("Digite um valor inteiro: "))
    if num == 999:
        break
    cont += 1
    soma += num

print(f"\033[32mForam digitados {cont} números e a soma de todos os números sem o flag foi {soma}.\033[m")