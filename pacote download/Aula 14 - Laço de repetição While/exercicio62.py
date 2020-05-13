""" Desafio 62. Melhore o programa do desafio 61, pedindo para o usuário ver mais alguns termos...
quando o usuário falar quero ver mais "0" termos ai o programa acaba """

i = int(input("O primeiro termo da PA é: "))
r = int(input("A razão da PA é: "))
decimo1 = i + (11 - 1) * r
c = i
quer_sair = False

print("Os dez primeiros termos da PA são:")
while c != decimo1:
    print("{}".format(c), end=" ")
    c = c + r

while not quer_sair:
    mais = int(input("\nQuantos termos mais da PA você deseja? "))
    para = c + ((mais + 1) - 1) * r
    if mais != 0:
        while c != para:
            print("{}".format(c), end=" ")
            c = c + r
    else:
        quer_sair = True

print("Fim do programa! Obrigado")




