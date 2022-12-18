salario = float(input("Qual é o salário do funcionário? R$"))
if salario <= 1250:
    aumento = salario + (salario*15/100)
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, aumento))
else:
    aumento1 = salario + (salario*10/100)
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, aumento1)) 
