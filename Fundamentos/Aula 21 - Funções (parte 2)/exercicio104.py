"""Desafio 104. Faça um programa parecido com o input do Python. Ele receba um inteiro e valida se o número digitado foi
realmente um inteiro. Se não for, ele pede para o usuário digitar novamente... """

def leianInt(msg):
    inteiro = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            inteiro = True
        else:
            print('ERRO! Valor foi digitado incorretamente!')
        if inteiro:
            break
    return valor



n = leianInt('Digite um número: ')
print(f'O valor digitado foi {n}!')

