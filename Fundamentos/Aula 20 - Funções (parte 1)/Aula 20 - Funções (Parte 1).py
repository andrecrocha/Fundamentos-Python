# funções e parâmetros, quando sua programação virar uma rotina voce usa funções e parâmetros
# primeiro se define a rotina com o comando def
# os parâmetros ficam entre parênteses
def sub(a, b):
    s = a - b
    print(s)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)

def contador(* num):
    print(num)
    tam = len(num)
    print(tam)

def valores(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos += 1

# Programa principal
sub(4, 1)
sub(10, 5)
sub(8, 9)
# eu posso mudar a ordem dos parametros dentro da função que eu chamar
soma(b=5, a=3)
print()
# há uma funcionalidade que o Python reconhece o número de parâmetros que recebe... veja na função contador()
contador(4, 5, 6, 7)
contador(9, 0, 0, 4)
contador(1, 3, 4, 5, 6, 7, 4, 3)
# funções e rotina com lista, no caso uso a função valores
numeros = [4, 5, 6, 6, 7]
print(numeros)
valores(numeros)
print()
print(numeros)





