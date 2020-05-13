""" Desafio 72. Faça um programa com um tupla preenchida com número por extenso de 0 até 20. Quando o usuário digitar
um número, mostre ele por extenso na tela. """

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
"quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

n = int(input("Digite um número de 0 a 20 para mostrar seu nome por extenso: "))
while n < 0 or n > 20:
    n = int(input("Número digitado incorretamente. Tente mais uma vez: "))

print(f"O número {n} por extenso é {numeros[n]}.")


