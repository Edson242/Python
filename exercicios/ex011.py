#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e quqnatidade de tinta necessária para pintá-la, sabendo que cada 1L de tinta, pinta uma área de 2m².

l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
d = l * a
t = d / 2
print("Sua parede tem a dimenção de {}x{} e sua área é de {:.3f}m².\nPara pintar essa parede, você precisará de {:.4f}l de tinta.".format(l, a, d, t))
