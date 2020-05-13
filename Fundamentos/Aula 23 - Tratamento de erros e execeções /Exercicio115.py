"""Desafio 115. Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples. O sistema só vai ter duas opções: cadastrar novas pessoas ou sair do sistema."""
import modandre as m
from time import sleep


while True:
    manipulador = open('arquivos')
    print()
    m.escreva(f'{"DIRETÓRIO DE DADOS":^40}')
    print("[0] Visualizar a lista completa\n"
          "[1] Adicionar uma pessoa à lista\n"
          "[2] Sair do sistema")

    opcao = input("O que você deseja fazer? ")
    while opcao != "0" and opcao != "1" and opcao != "2":
        opcao = input("\033[31;1mOpção inválida. Digite novamente:\033[m")

    print()

    if opcao == "0":
        print("Abrindo a lista. Aguarde...")
        print()
        sleep(1)
        m.leiaarquivo('arquivos')

    elif opcao == "1":
        print("Abrindo o leitor. Aguarde...")
        sleep(1)
        nome = m.leiaNome("Digite o nome da pessoa: ")
        idade = m.leiaIdade("Qual é a idade da pessoa: ")
        with open('arquivos', 'a') as manipulador:
            manipulador.write("\n")
            manipulador.write(nome)
            manipulador.write(";")
            manipulador.write(str(idade))
        manipulador.close()

    else:
        break

print('\033[32mPrograma encerrado. Volte Sempre!\033[m')














