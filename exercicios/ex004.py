#Faça um progama que leia algo e mostre seu tipo primitivo e todas as informações possiveis sobre ela.

a = input("Digita algo: ")
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um numero? ", a.isnumeric())
print("É alfabetico? ", a.isalpha())
print("É alfanumerico? ", a.isalnum())
print("Está em maiúsculo? ", a.isupper())
print("Está minúscula? ", a.islower())
print("Está capitalizada? ", a.istitle())