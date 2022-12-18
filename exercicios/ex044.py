print("=" * 10, "LOJAS SILVEIRA", "=" * 10)
preço = float(input("Preço das compras: R$"))
pagamento = int(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? """))
if pagamento == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, preço - (preço * (10/100))))
elif pagamento == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, preço - (preço * (5/100))))
elif pagamento == 3:
    parcela = preço / 2
    print("Sua compra será parcelada em 2x de R${:.2f} totalizando R${:.2f} SEM JUROS!".format(parcela, preço))
elif pagamento == 4:
    parcelas = int(input("Quantas parcelas? "))
    totparc = preço + (preço * 20/100)
    parcela = totparc / parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} totalizando R${:.2f} COM JUROS!".format(parcelas, parcela, totparc))
else:
    print("OPÇÃO INVÁLIDA DE PAGAMENTO, TENTE NOVAMENTE!")
    