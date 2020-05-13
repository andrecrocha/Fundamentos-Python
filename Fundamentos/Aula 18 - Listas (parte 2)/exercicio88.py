""" Desafio 88. Gerar n jogos da Mega-Sena, e pedir para o programa mostrar esses números na tela"""
from random import randint
from time import sleep
print("===" * 20)
print()
print("PALPITEIRO DA MEGA-SENA DO ANDRÉ")
print()
print("===" * 20)
n = int(input("Quantos jogos da MEGA-SENA você quer sortear? "))
jogo = []
print("Aguarde, meu programa está pensando em bons palpites...")
sleep(2)
print("LÁ VAI...")
sleep(1)
for l in range(0, n):
    for c in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        else:
            while num in jogo:
                num = randint(1, 60)
            jogo.append(num)
    jogo.sort()
    print(f"\033[1;34mJogo {l+1}: {jogo}\033[m")
    sleep(1)
    jogo.clear()

print()
print(f"\033[1;32mAGORA É SO APOSTAR!! BOA SORTE!!\033[m")


