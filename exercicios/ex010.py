#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares eka pode comprar. US$3.27

n = float(input("Quanto dinheiro você tem na carteira? R$"))
d = n / 5.42
e = n / 5.43
print("Com R${:.2f} você pode comprar US${:.2f} ou €${:.2f}".format(n, d, e))
