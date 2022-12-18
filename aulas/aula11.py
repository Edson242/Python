nome = str(input("Qual seu nome? ")).split()
if nome == "Edson":
    print("Que belo nome!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no brasil.")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}".format(nome))