#Desafio 08. colocar uma medida em metros e convertê-la para outras medidas
m = int(input("Colocar a medida em metros: "))
print("A medida de {} corresponde a:".format(m))
print(m/1000) + ("km")
print(m/100) +("hm")
print(m/10) + ("dam")
print(m*10) + ("dm")
print(m*100) + ("cm")
print(m*1000) + ("mm")