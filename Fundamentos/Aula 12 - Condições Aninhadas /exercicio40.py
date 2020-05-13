""" Desafio 40. Crie um programa que leia a média de duas notas de um aluno, mostrando uma
mensagem ao final de acordo com a média atingida. Se menos de 5.0 reprovado, se entre
5.0 e 6.9, recuperação, se maior que 7.0, aprovado!"""
n1 = float(input("Qual foi a primeira nota?: "))
n2 = float(input("Qual foi a segunda nota?: "))
media = (n1+n2) / 2
if media < 5.0:
  print("\033[31;1mInfelizmente sua média foi {:.2f} e você foi REPROVADO!".format(media))
elif media >= 5.0 and media <= 6.9:
  print("\033[33;1mSua média foi {:.2f} e você está de RECUPERAÇÃO!".format(media))
else:
  print("\033[32;1mSua média foi {:.2f} e você foi APROVADO! Parabéns!\033[m".format(media))
print ("Obrigado!")