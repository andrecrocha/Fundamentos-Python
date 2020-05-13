"""Desafio 92. Crie um programa que leia nome, ano de nascimento e carteira de trabalho de e cadastre-os (com idade), em
um diconário, se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule com qtos anos a pessoas vai se aposentar... sendo a contribuição de 35 anos """

from datetime import date
ano = date.today().year
pessoa = dict()

pessoa["Nome"] = str(input("Digite o nome da pessoa: "))
anonasc = int(input("Qual é seu ano de nascimento: "))
pessoa["Idade"] = ano - anonasc
pessoa["Carteira_de_trabalho"] = int(input("Digite o número da CPTS (0 não tem): "))
if pessoa["Carteira_de_trabalho"] != 0:
    pessoa["Ano_de_contratação"] = int(input("Qual foi o ano de contratação? "))
    pessoa["Salário"] = float(input("Qual foi seu salário? R$"))
    pessoa["Idade_para_aposentar"] = 35 - (ano - pessoa["Ano_de_contratação"]) + pessoa["Idade"]
print()
print("==" * 20, "DADOS DA PESSOA", "==" * 20)
for k, v in pessoa.items():
    print(f'{k} é {v}')





