""" Desafio 59. Crie um programa que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior
[4] novos números [5] sair do programa. """

from time import sleep
print("---- Calculadora do André ----")
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
menu = 1

while menu != 5:
    print("")
    menu = int(input("""  ----- MENU DE OPÇÕES -----
[1] Somar
[2] Multiplicar
[3] Descobrir o maior número
[4] Novos números
[5] Sair do programa
"""))
    print("\033[34mPROCESSANDO... \033[m")
    sleep(1)
    if menu == 1:
        print("A soma de {} e {} é igual a {:.2f}".format(v1, v2, v1 + v2))
        menu = int(input("Se desejar sair digite 5: "))
    elif menu == 2:
        print("{} multiplicado por {} é igual {:.2f}".format(v1, v2, v1 * v2))
        menu = int(input("Se desejar sair digite 5: "))
    elif menu == 3:
        if v1 > v2:
            print("{} é maior que {}".format(v1, v2))
            menu = int(input("Se desejar sair digite 5: "))
        elif v2 > v1:
            print("{} é maior que {}".format(v2, v1))
            menu = int(input("Se desejar sair digite 5: "))
        else:
            print("Os dois números são iguais!")
            menu = int(input("Se desejar sair digite 5: "))
    elif menu == 4:
        print("Informe novamente os números...")
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))
    elif menu == 5:
        print("Finalizando...")
    else:
        print("Código inválido... Tente novamente!")

print("--" * 20)
print("\033[1;32mObrigado por utilizar minha calculadora!\033[m")

