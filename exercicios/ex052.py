print("-=-" * 5 + " Bem vindo ao detector de números primos " + "-=-" * 5)
número = int(input("Digite um número: "))
tot = 0
for c in range(1, número + 1):
    if número % c == 0:
        print('\033[33m', end="")
        tot += 1
    else:
        print('\033[31m', end="")
    print("{} ".format(c), end="")
print("\n\033[mO número {} foi divisível por {} vezes".format(número, tot))
if tot == 2:
    print("E por isso ele é primo !")
else:
    print("E por isso ele não é primo !")