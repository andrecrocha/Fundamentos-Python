#Desafio 19. Mostrar e sortear o nome de algum aluno dentre 4, e depois sortear uma sequência
import random
lista = ['maria', 'joão', 'elisa', 'paulo']
print("Os alunos são: {}".format(lista))
print("O aluno escolhido para fazer o exercício é: {}".format(random.choice(lista)))
random.shuffle(lista)
print("A sequência dos aluno é:{}".format(lista))