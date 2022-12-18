nome = str(input("Qual seu nome? ")).title()
if nome == "Edson":
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    m = (n1+n2)/2
    if m <= 5.0:
        print("Situação: REPROVADO!\nSua média foi de {:.1f}".format(m))
    elif m >= 5.0 and 6.9:
        print("Situação: RECUPERAÇÃO!\nSua média foi de {:.1f}".format(m))
    elif m >= 7.0:
        print("Sitação: APROVADO! Parabéns!\nSua média foi de {:.1f}".format(m))
elif nome == "Ana":
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    m = (n1+n2)/2
    if m <= 6.0:
        print("Situação: REPROVADO!\nSua média foi de {:.1f}".format(m))
    elif m >= 6.0 and 7.9:
        print("Situação: RECUPERAÇÃO!\nSua média foi de {:.1f}".format(m))
    elif m >= 8.0:
        print("Sitação: APROVADO! Parabéns!\nSua média foi de {:.1f}".format(m))
else:
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    m = (n1+n2)/2
    if m <= 4.0:
        print("Situação: REPROVADO!\nSua média foi de {:.1f}".format(m))
    elif m >= 4.0 and 5.9:
        print("Situação: RECUPERAÇÃO!\nSua média foi de {:.1f}".format(m))
    elif m >= 6.0:
        print("Sitação: APROVADO! Parabéns!\nSua média foi de {:.1f}".format(m))
