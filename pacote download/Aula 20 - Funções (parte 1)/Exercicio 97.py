"""Desafio 97. Faça um programa com a função chamada escreva() e printe algo na tela com uma moldura de acordo com o tamanho
da frase"""

def escreva(txt):
    print("=" * len(txt))
    print(txt)
    print("=" * len(txt))

# Programa principal
escreva("A lua está linda")
escreva("O céu está bonito")
escreva("O rio é lindo, e a paisagem também, mas tudo não passa de uma ilusão dos sentidos")
escreva("Tchau")
