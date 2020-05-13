"""Desafio 45. JOGO. Crie um computador que jogue Jokenpô com você."""
from random import randint
from time import sleep
jogador = int(input("""Escolha Pedra, Papel ou Tesoura:
0 = Pedra
1 = Papel
2 = Tesoura
"""))
print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PO...")
sleep(1)
comp = randint(0,2)
if jogador == comp:
  if comp == 0:
    print("O jogo empatou, porque ambos escolheram PEDRA.")
  elif comp == 1:
    print("O jogo empatou, porque ambos escolheram PAPEL.")
  elif comp == 2:
    print("O jogo empatou, porque ambos escolheram TESOURA.")
elif jogador == 1 and comp == 0 or jogador == 0 and comp == 2 or jogador == 2 and comp == 1:
  if jogador == 1 and comp == 0:
    print("Você venceu! Escolheu PAPEL e o computador escolheu PEDRA!")
  elif jogador == 0 and comp == 2:
    print("Você venceu! Escolheu PEDRA e o computador escolheu TESOURA!")
  elif jogador == 2 and comp == 1:
    print("Você venceu! Escolheu TESOURA e o computador escolheu PAPEL!")
elif comp == 1 and jogador == 0 or comp == 0 and jogador == 2 or comp == 2 and jogador == 1:
  if comp == 1 and jogador == 0:
    print("Você perdeu! O computador escolheu PAPEL e você PEDRA!")
  elif comp == 0 and jogador == 2:
    print("Você perdeu! O computador escolheu PEDRA e você escolheu TESOURA!")
  elif comp == 2 and jogador == 1:
    print("Você perdeu! O computador escolheu TESOURA e você escolheu PEDRA!")
print("Obrigado por participar do meu game!")