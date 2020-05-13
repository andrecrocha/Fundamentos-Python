# Aula de dicionários. Ao contrário das listas, os dicionários podem ter "itens literais"
pessoa = {"nome": "André", "idade": 23, "sexo": "M"}
print(pessoa)
print(pessoa["nome"])
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos e é do sexo {pessoa["sexo"]}') #para printar tem q ter aspas duplas
print()
print(pessoa.keys()) #mostrar as categorias
print(pessoa.values()) #mostrar os valores
print(pessoa.items()) #mostrar todos os itens
print()
# usar laços de repetição para mostrar os itens
for k in pessoa.keys():
    print(k)
# só os valores
print()
for v in pessoa.values():
    print(v)
#os itens completos, com a key e os values
for k, v in pessoa.items():
    print(f'{k} = {v}')
# eu posso deletar uma key do diconário:
del pessoa['sexo']
print()
print(pessoa)
# e depois adicionar um elemento:
pessoa["peso"] = 98.5
print(pessoa)
print()

# podemos também colocar dicionários dentro de listas
equipes = []
time1 = {"nome": "Corinthians", "mascote": "Mosqueteiro"}
time2 = {"nome": "Palmeiras", "mascote": "Porco"}
time3 = {"nome": "São Paulo", "mascote": "Santo"}
equipes.append(time1)
equipes.append(time2)
equipes.append(time3)
print(equipes)
print(equipes[0]["nome"])
print((equipes[1]["mascote"]))

# não se pode fatiar os elementos de um dicionário. Para copiar há um método interno, chamado copy()
alunos = list()
nomes = dict()
for c in range(0,3):
    nomes["nome"] = str(input("Digite o nome do aluno: "))
    nomes["nota"] = int(input("Digite a nota do aluno: "))
    alunos.append(nomes.copy())
print(alunos)
for a in alunos:
    for v in a.values():
        print(v)


