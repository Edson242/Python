viagem = int(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {:.1f}Km.".format(viagem))
if viagem <= 200:
    print("E o preço da sua passagem será de R${:.2f}".format(0.50*viagem))
else:
    print("E o preço da sua passagem será de R${:.2f}".format(0.45*viagem))
    