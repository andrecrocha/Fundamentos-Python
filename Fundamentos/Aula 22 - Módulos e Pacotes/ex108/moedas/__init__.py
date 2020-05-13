def moeda(v):
    nome = str(v)
    nome1 = nome.replace(".", ",")
    return f'R${nome1}'


def dobro(v, formatar=False):
    if formatar:
        return moeda(v * 2)
    else:
        return f'{v * 2:.2f}'


def metade(v, formatar=False):
    if formatar:
        return moeda(v / 2)
    else:
        return f'{v / 2:.2f}'


def aumentar(v, porcentagem, formatar=False):
    if formatar:
        return moeda(v + v * porcentagem / 100)
    else:
        return f'{v + v * porcentagem / 100:.2f}'


def diminuir(v, porcentagem, formatar=False):
    if formatar:
        return moeda(v - v * porcentagem / 100)
    else:
        return f'{v - v * porcentagem / 100:.2f}'

def resumo(v, aum, dim):
    print("==" * 20)
    print("  ANALISANDO O VALOR APRESENTADO  ")
    print("==" * 20)
    print(f'Preço analisado:      {moeda(v)}')
    print(f'Dobro do preço:       {dobro(v, True)}')
    print(f'Metade do preço:      {metade(v, True)}')
    print(f'{aum}% de aumento:      {aumentar(v, aum, True)}')
    print(f'{dim}% de diminuição:   {diminuir(v, dim, True)}')






