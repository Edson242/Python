peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual sua altura? (m) "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
# if 18.5 <= imc < 25: -> Pode se fazer assim tbm...
if imc < 18.5:
    print("Você está ABAIXO DO PESO NORMAL!")
elif imc <= 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL!")
elif imc <= 30:
    print("Você está na faixa de SOBREPESO!")
elif imc <= 40:
    print("Você está na faixa de OBESIDADE!")
elif imc > 40:
    print("Você está na faixa de OBESIDADE MÓRBIDA, CUIDADO!")