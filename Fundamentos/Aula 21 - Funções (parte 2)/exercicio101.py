"""Desafio 101. Crie um programa que tenha uma função chamada voto(). Ele vai receber o parâmetro de o ano de nascimento
de uma pessoa, retornando um valor literal, VOTO OBRIGATÓRIO, VOTO OPCIONAL, NÃO VOTA"""

def voto(ano):
    from datetime import date   # Você pode fazer a importação dentro de uma função
    atual = date.today().year
    idade = atual - ano
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: NÃO VOTA!'


# Programa Principal


n = int(input("Em que ano você nasceu? "))
print(voto(n))













