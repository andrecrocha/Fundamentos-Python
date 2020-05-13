"""Desafio 113. Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de
um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma finalidade."""

def leiaInt(msg):
    válido = False
    while not válido:
        try:
            numero = int(input(msg))
        except KeyboardInterrupt:
            print(f'\033[1;33mO usuário preferiu não informar os dados\033[m')
            numero = 0
            válido = True
        except:
            print(f'\033[1;31mERRO! Digite um número inteiro válido!\033[m')
        else:
            print(f'\033[1;34mNúmero armazenado corretamente!\033[m')
            válido = True

    return numero


def leiafloat (msg):
    válido = False
    while not válido:
        try:
            real = float(input(msg))
        except KeyboardInterrupt:
            print(f'\033[1;33mO usuário preferiu não informar os dados\033[m')
            real = 0
            válido = True
        except Exception as error:
            print(f'\033[1;31mERRO! Digite um número real válido!\033[m')
        else:
            print(f'\033[1;34mNúmero armazenado corretamente!\033[m')
            válido = True

    return real


#Programa Principal

numero = leiaInt('Digite um número inteiro: ')
real = leiafloat('Digite um número real válido: ')
print()
print(f'Os números armazenados foram {numero} e {real}!')




