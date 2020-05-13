"""Desafio 83. Validar uma expressão matemática"""

expressao = str(input("Escreva uma expressão matemática: "))
simbolos = list()
for elemento in expressao:
    if elemento == "(":
        simbolos.append("(")
    elif elemento == ")":
        if len(simbolos) > 0:
            simbolos.pop()
        else:
            simbolos.append(")")
            break

if len(simbolos) == 0:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")
