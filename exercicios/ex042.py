print("-=-" * 25)
print("Analisador de Triângulos")
print("-=-" * 25)
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a<b+c and b<a+c and c<a+b:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end="")
    if a == b == c:
        print("Equilátero!")
    elif a != b != c != a:
        print("Escaleno!")
    else:
        print("Isósceles!")
else:
    print("Os segmentos NÃO PODEM FORMAR triângulos!")
print("-=-" * 25)
