"""Desafio 102. Crie um programa que tenha uma função fatorial(), que receba dois parâmetros. O primeiro que indique
o número a calcular e o outro chamado show, que será um valor lógico indicando se será mostrado na ou não na tela o
processo de cálculo do fatorial."""

def fatorial(n = 1, show=False):
    """
    Calcula o fatorial de um número n.
    :param n: número a ser calculado
    :param show: (True) mostra a conta
    :return: O valor de um fatorial de um número n.
    """
    mult = 1
    for c in range(n, 0, -1):
        mult *= c
        if show == True:
            if c > 1:
                print(f'{c} x ', end=" ")
            else:
                print(f'{c} =', end=" ")
    return mult


print(fatorial(5, show=True))
print(fatorial(6))
print(fatorial(4, True))
help(fatorial)

