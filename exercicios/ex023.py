num = int(input("Informe um número: "))
#Dividir em 4 partes
u = num // 1 % 10
#Primeira parte
d = num // 10 % 10
#Segunda Parte
c = num // 100 % 10
#Terceira Parte
m = num // 1000 % 10
#Quarta Parte

print("Analisando o múmero {}".format(num))
print("Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}".format(u, d, c, m))