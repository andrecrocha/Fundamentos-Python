# ajuda interativa, função help
# help(print)
# fazer uma docstring de uma função, aspas triplas depois do def
def area(larg, comp):
    """
    -> Esta função calcula a aréa de um terreno.
    :param larg: medida da largura
    :param comp: medida do comprimento
    :return: sem retorno
    Função criada por André Campos Rocha
    """
    c = larg * comp
    print(f'A área do terreno é de {c:.2f} m2.')
    print("---" * 20)

help(area)

# Parâmetros opcionais. O parâmetro recebe um valor padrão, que não precisa ser digitado pelo usuário. por exemplo...
# na função def soma(a, b, c), eu posso colocar def soma (a, b, c=0), sendo 0 o valor padrão de c... isso ocorre p.e
# com a função print(), cujo valor padrão pro end é "\n", e por aí vai...

# Escopo de variável: global e local

# Retorno de valores... função -> return... 

