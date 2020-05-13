#Desafio 07. calcular a média aritmética das notas de um aluno
nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))
#tem que observar a ordem de precedência dos operadores aritméticos. Por que isso que vem o parenteses na soma
media = (nota1 + nota2)/ 2
print("A média das notas é no valor de {:.1f}".format (media))
