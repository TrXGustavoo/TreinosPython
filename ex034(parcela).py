print('{:=^40}'.format(' LOJAS '))
preco = float(input('Valor  total da compra: R$'))
print("""FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
op = int(input('Qual é a opção? '))
if op == 1:
    Vfinal = preco - (preco * 0.10)
    print('Sua compra de {} vai custar {} no final'.format(preco, Vfinal))
elif op == 2:
    Vfinal = preco - (preco * 0.05)
    print('Sua compra de {} vai custar {} no final'.format(preco, Vfinal))
elif op == 3:
    Vfinal = preco
    print('Sua compra de {} vai custar {} no final'.format(preco, Vfinal))
elif op == 4:
    parc = int(input('Quantas parcelar? '))
    parcela = (preco + (preco * 0.20)) / parc
    Vfinal = preco + preco * 0.20
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(parc, parcela))
    print('Sua compra de {} vai custar {} no final'.format(preco, Vfinal))