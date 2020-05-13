def moeda(v):
    return f'R${v:>5.2f}'.replace('.', ',')


def dobro(v, formatar=False):
    res = v * 2
    return res if not formatar else moeda(res)


def metade(v, formatar=False):
    res = v / 2
    return res if not formatar else moeda(res)


def aumentar(v, porcentagem, formatar=False):
    res = v + v * porcentagem / 100
    return res if not formatar else moeda(res)


def diminuir(v, porcentagem, formatar=False):
    res = v - v * porcentagem / 100
    return res if not formatar else moeda(res)


def resumo(v, aum, dim):
    print("==" * 20)
    print("  ANALISANDO O VALOR APRESENTADO  ")
    print("==" * 20)
    print(f'Preço analisado:    \t{moeda(v)}')
    print(f'Dobro do preço:      \t{dobro(v, True)}')
    print(f'Metade do preço:     \t{metade(v, True)}')
    print(f'{aum}% de aumento:     \t{aumentar(v, aum, True)}')
    print(f'{dim}% de diminuição:  \t{diminuir(v, dim, True)}')