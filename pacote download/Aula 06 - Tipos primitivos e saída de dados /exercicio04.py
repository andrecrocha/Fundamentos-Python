#exercicio quatro: mostrar o tipo primitivo de algo que foi digitado
a = (input("Digite algo: "))
print("O tipo primitivo de algo é", type(a))
print("Só tem espaços?", a.isspace())
print("é um número?", a.isnumeric())
print("é alfabético?", a.isalpha())
print("é alfanumérico?", a.isalnum())
print("Está em maiúscula?", a.isupper())
print("Está em minúscula?", a.islower())

"""Para o python, as funções upper e lower só darão True se todos os caracteres
forem de um mesmo tipo. Senão falamos de capitalização, quando tem os dois cara
cteres
"""
print("Está capitalizado?", a.istitle())
