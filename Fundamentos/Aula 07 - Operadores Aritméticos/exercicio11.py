#exercicio 11: calculcar a largura e a altura de uma parede em metros e descobrir o quanto de tinta é necessário
#para pintar essa parede, dado 1l de tinta pinta 2 metros quadrados de parede.
print("-----CALCULANDO A TINTA DA PAREDE-----")

larg = float(input("Escreva a largura da parede: "))
alt = float(input("Escreva a altura da parede: "))
area = (larg) * (alt)
tinta = (area) / 2

print("Sua parede tem a dimensão de {} x {} e sua área é de {} m2.".format(larg, alt, area))
print("A quantidade de tinta necessária para pintá-la é {:.3f} litros de tinta.".format(tinta))