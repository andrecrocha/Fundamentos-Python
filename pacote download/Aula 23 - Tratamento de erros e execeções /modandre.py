def leiaIdade(msg):
    válido = False
    while not válido:
        try:
            idade = int(input(msg))
        except:
            print(f'\033[1;31mERRO! Digite uma idade válida!\033[m')
        else:
            print(f'\033[1;34mDados armazenados corretamente!\033[m')
            válido = True

    return idade


def escreva(txt):
    print("=" * len(txt))
    print(txt)
    print("=" * len(txt))


def leiaNome(msg):
    nome = input(msg).strip().title()
    while nome == "":
        print(f'\033[1;31mNome não digitado corretamente. Tente novamente!\033[m')
        nome = input(msg).strip().title()

    return nome


def reduza(nome):
    resp = " " * (25 - len(nome))
    return resp

def leiaarquivo(arq):
    a = open(arq, 'rt')
    print(escreva(f'{"LISTA DE NOMES":^40}'))
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    a.close()






