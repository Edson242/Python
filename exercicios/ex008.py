#Escreva um programa que lçeia um valor em metros e exiba convertido em km, hm, dam, dm, cm, mm.
n = float(input("Uma distância em metros: "))
km = n / 1000
hm = n * 1
dam = n * 1
dm = n * 10
cm = n * 100
mm = n * 1000
print("A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{}cm \n{}mm".format(n, km, hm, dam, dm, cm, mm))
