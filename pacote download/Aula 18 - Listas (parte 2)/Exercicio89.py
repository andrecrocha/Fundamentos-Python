""" Desafio 89. Ler nome e duas notas de dois alunos. Dar ao final o boletim completo, com o nome e a média das notas.
Depois perguntar ao programa de qual aluno o programa quer ver as notas. """

lista = list()

while True:
    nome = str(input("Qual é o nome do aluno? ")).strip()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, nota1, nota2, media])
    sair = str(input("Você quer continuar? [S/N]?")).upper().strip()
    while sair not in "SN":
        sair = str(input("Código errado. Tente novamente: ")).upper().strip()
    if sair == "N":
        break

print()
print("*-" * 10, " BOLETIM COMPLETO ", "*-" * 10)
print()
print("{:<8}{:<10}{:>8}".format("No", "NOME", "MÉDIA"))
for i, c in enumerate(lista):
    print(f"{i:<8}{c[0]:<10}{c[3]:>8.2f}")
print()
print("*-" * 30)
print()
while True:
    num = int(input("De qual aluno você quer ver as notas individuais? (999 para parar) "))
    if num == 999:
        break
    print(f"As notas individuais de {lista[num][0]} foram {lista[num][1]} e {lista[num][2]}!")
print()
print("OBRIGADO, VOLTE SEMPRE!")


