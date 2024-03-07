Vcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = Vcasa / (anos * 12)

if parcela < (salario * 0.30):
    print('Para pagar uma casa de R${:.2f} em {} anos a prstação será de R${:.2f}\n Empréstimo pode ser \033[32mCONCEDIDO\033[m'.format(Vcasa, anos, parcela))
else:
    print('Para pagar uma casa de R${} em {} anos a prstação será de R${:.2f}\n Empréstimo \033[31mNEGADO\033[m !'.format(Vcasa, anos, parcela))
    