#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input("Informe a temperatura em ºC: "))
f = ((9 * c) / 5) + 32
k = c + 273
print("A temperatura de {}ºC corresponde a {}ºF e {}ºK!".format(c, f, k))
