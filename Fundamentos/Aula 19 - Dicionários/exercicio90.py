"""Desafio 90. Ler nome e média de um aluno e printar a situação( aprovado > 7.0, reprovado < 7.0 )"""
aluno = {}
aluno["nome"] = str(input("Qual o nome do aluno: "))
aluno["média"]  = float(input("Qual a média do aluno: "))
if aluno["média"] > 7:
    aluno["situação"] = "aprovado"
else:
    aluno["situação"] = "reprovado"

for e, v in aluno.items():
    if e == "nome":
        print(f"O {e} do aluno é {v}")
    else:
        print(f"A {e} é {v}")

