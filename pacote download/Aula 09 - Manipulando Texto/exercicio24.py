#Desafio 24. Você nasceu em um cidade que começa com a palavra Santo?
nome = str(input("Digite o nome da cidade: ")).strip()
nomemin = nome.capitalize()
divisao = nomemin.split()
print("Santo" in divisao[0])
# outro método
# linha 2 -> print(nome[:5].upper == 'SANTO')