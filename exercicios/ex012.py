#Faça um algoritmo que leia o preço do produto e mostre seu novo preço, com 5% de desconto

p = float(input("Qual é o preço do produto? R$ "))
#novo = p - (p * 5 / 100)
d1 = 5 / 100
d2 = p * d1
d3 = p - d2
print("O produto que custava R${}, na promoção com 5% de desconto vai custar R${:.2f}".format(p, d3))
