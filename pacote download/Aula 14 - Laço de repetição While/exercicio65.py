""" Crie um programa que leia números inteiros e a cada lida pergunte se o usuário quer continuar. Mostre qual foi a média
e o maior e o menor valor lidos. """

cont = soma = maior = menor = 0
sair = " "
while sair != "S":
    num = int(input("Escreva um número inteiro: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    sair = str(input("Você deseja sair? [S/N]: ")).strip().upper()
    while sair != "N" and sair != "S":
        print("\033[1;31mCódigo errado. Tente novamente!\033[m")
        sair = str(input("Você deseja sair? [S/N]: ")).strip().upper()

media = soma / cont
print("\033[1;32mVocê analisou {} números e a média entre eles é {:.2f}.\033[m".format(cont, media))
print("\033[1;34mO maior número é {} e o menor número é {}.\033[m".format(maior, menor))
print("\033[1;35mObrigado!!\033[m")




