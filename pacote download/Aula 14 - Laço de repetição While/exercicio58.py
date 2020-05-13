""" Desafio 58. Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários até vencer."""

from random import randint
num_pc = randint(0, 10)
num_usu = 1
cont = 0

while num_pc != num_usu:
    num_usu = int(input("Digite um número e tente acertar: "))
    cont += 1
    if num_pc != num_usu:
        print("Você errou! Tente novamente!")
    else:
        print("\033[33mPARABÉNS! VOCÊ ACERTOU!\033[m")
print("\033[1;34mPara isso foram necessárias {} tentativas.\033[m".format(cont))

