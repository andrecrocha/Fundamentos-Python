""" Desafio 73. Crie um tupla com a colocação do brasileirão. Depois mostre: a) os 5 primeiros colocados; b) os últimos 4 colocados
da tabela; c) lista com os times em ordem alfabética d) em que lugar está a Chapecoense. """

brasileirao = ("Flamengo", "Palmeiras", "São Paulo", "Grêmio", "Cruzeiro", "Atlético-MG", "Corinthians", "Santos", "Atlético-PR",
"Goiás", "Vasco", "CSA", "Avaí", "Botafogo", "Bahia", "Internacional", "Atlético-GO", "Chapecoense", "Fluminense", "Sport")

print(f"Os cinco primeiros colocados são {brasileirao[0:5]}.") # a
print(f"Os últimos quatro colocados são {brasileirao[-4:]}.") # b
print(f"Os times em ordem alfabética: {sorted(brasileirao)}.") #c
print("A Chapecoense está na {}a posição".format(brasileirao.index("Chapecoense") + 1))
