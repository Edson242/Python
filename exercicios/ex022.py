import time
nome = str(input("Digite seu nome completo: ")).strip()
# Nome em letras maiúsculas
mai = nome.upper()
# Nome em letras minúsculas
min = nome.lower()
# Número de Letras
letras = len(nome)-nome.count(" ")
# Número de Letras do Primeiro Nome
letras1 = nome.split()
print("Analisando seu nome...")
time.sleep(3)
print("Seu nome em maiúsculo é {}".format(mai))
print("Seu nome em minúsculas é {}".format(min))
print("Seu nome tem a todo {} letras".format(letras))
print("Seu primeiro nome é {} e ele tem {} letras".format(letras1[0], len(letras1[0])))