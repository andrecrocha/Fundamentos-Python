""" Desafio 67. Programa que mostre a tabuada de vários números. Quando o número for negativo saia do programa."""

while True:
    num = int(input("Digite um número inteiro para mostrar sua tabuada: "))
    if num < 0:
        break
    print("---" * 10)
    for c in range (1, 11):
        print(f"{num} x {c} = {num * c}")
    print("---" * 10)
print("FIM DO PROGRAMA, OBRIGADO!")
