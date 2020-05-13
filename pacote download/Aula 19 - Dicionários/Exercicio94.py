"""Desafio 94. Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final mostre: a) quantas pessoas foram cadastradas; b) a média de idade do grupo
c) Uma lista com todas as mulheres; d) uma lista com todas as pessoas com a idade acima da média"""

pessoa = {}
arquivo = []
tot = 0
while True:
    print("==" * 30)
    pessoa["nome"] = str(input("Qual é o nome da pessoa? ")).strip()
    pessoa["sexo"] = str(input(f'Qual é o sexo de {pessoa["nome"]} [M/F]?')).strip().upper()
    while pessoa["sexo"] not in "MF":
        pessoa["sexo"] = input("Sexo inválido. Digite novamente!")
    pessoa["idade"] = int(input(f'Qual é a idade de {pessoa["nome"]}? '))
    arquivo.append(pessoa.copy())
    pessoa.clear()
    sair = input("Você deseja sair? [S/N]?").strip().upper()
    while sair not in "SN":
        sair = input("Código errado. Tente novamente: ").strip().upper()
    if sair == "S":
        break
print("==" * 30)
print(arquivo)
print(("==" * 30))
print(f'Foram {len(arquivo)} pessoas cadastradas.')
for c in arquivo:
    tot += c["idade"]
media = tot / len(arquivo)
print(f'A médida de idade do grupo foi {media:.2f}.')
print(f'As mulheres cadastradas foram', end=" ")
for c in arquivo:
    if c["sexo"] == "F":
        print(f'{c["nome"]}', end="  ")
print('\nOs dados das pessoas com idade acima da média foram: ')
for c in arquivo:
    if c["idade"] > media:
        print(c)











