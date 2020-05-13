"""Desafio 96. Calcular area de um terreno com função"""
def area(larg, comp):
    c = larg * comp
    print(f'A área do terreno é de {c:.2f} m2.')
    print("---" * 20)


while True:
    a = float(input("Qual o comprimento do terreno em metros quadrados: "))
    b = float(input("Qual a largura do terreno em metros quadrados: "))
    area(a, b)
    sair = input("Quer continuar? [S/N]").upper().strip()
    if sair == "N":
        break






