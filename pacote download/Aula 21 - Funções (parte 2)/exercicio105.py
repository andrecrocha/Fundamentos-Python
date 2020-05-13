"""Desafio 105. Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações: a) quantidade de notas; b) a maior nota; c) a menor nota; d) a média da turma
e) a situação (opcional). Adicione também as docstrings da função."""

def notas(* num, situacao=False):
    """
    Função que recebe notas de alunos e calcula a quantidade de notas recebidas,
    a maior e menor nota, a média das notas, e a situação da turma (opcional).
    :param num: notas
    :param situacao: situação de avaliação da turma
    :return: dicionário com os dados da turma
    """
    media = sum(num) / len(num)
    avaliacao = ""
    resumo = {"quantidade": len(num), "maior_nota": max(num), "menor": min(num), "media": media}
    if situacao:
        if media > 7:
            avaliacao = "BOA!"
        elif 5 <= media <= 7:
            avaliacao = "REGULAR!"
        else:
            avaliacao = "RUIM!"
        resumo["situação"] = avaliacao
    return resumo


print(notas(8, 9, 10, 9, 5, 5.6, situacao=True))
help(notas)







