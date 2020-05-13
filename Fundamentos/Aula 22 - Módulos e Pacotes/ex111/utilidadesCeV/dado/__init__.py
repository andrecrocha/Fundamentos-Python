# Valores monetários podem ser números inteiros (int) ou números flutuantes (float)

def leiadinheiro (msg):
    while True:
        num = input(msg).replace(',', '.').strip()
        if num.isalpha() or num.isalnum() or num == '':
            print(f'ERRO! {num} é um valor inválido')
        else:
            break

    return float(num)

