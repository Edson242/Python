valor = float(input("Qual valor da casa? R$"))
salario = float(input("Qual valor do seu sálario? R$"))
tempo = int(input("Em quantos anos pretende pagar isso? "))
parcela = (valor / tempo) / 12 
porcentagem = salario * (30/100)
if parcela > porcentagem:
    print("Seu empréstimo foi NEGADO! pois as parcelas ultrapassam 30% do seu salário.")
else:
    print("Seu empréstimo foi APROVADO e você pagará R${:.2f} por mês!".format(parcela))
