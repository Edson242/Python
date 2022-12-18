#Crie um programa que leia um número Real qualquer pelo teclado e mostre na sua tela a sua porção inteira.
from math import trunc

num = float(input("Digite um número: "))
#print("O valor digitado foi {} e sua porção ineira é {}".format(num, trunc(num)))

print("O valor digitado foi {} e sua porção inteira é {}".format(num, int(num)))