from datetime import date
sexo = str(input("Qual seu sexo? ")).lower()
if sexo == "masculino":
    ano = int(input("Ano de nascimento: "))
    anoA = date.today().year
    idade = anoA - ano
    if idade < 18:
        print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, anoA))
        print("Ainda faltam {} anos para o alistamento".format((18-idade )))
    elif idade > 18:
        print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, anoA))
        print("Você já deveria ter se listado há {} anos".format(idade-18))
        print("Seu alistamento foi em {}".format(anoA-(idade-18)))
    elif idade == 18:
        print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, anoA))
        print("Você deve se alistar IMEDIATAMENTE!")
else:
    print("Você não precisa fazer alistamento Militar Obrigatório!")
