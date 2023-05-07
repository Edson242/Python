termo = int(input("Primeiro Termo: "))
razão = int(input("Razão: "))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{}'.format(c), end=" -> ")
print("ACABOU")
