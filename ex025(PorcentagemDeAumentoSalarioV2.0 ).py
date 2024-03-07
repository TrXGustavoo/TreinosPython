salario = float(input('Qual é o salário do funcionário? R$'))
nSalario = 0
if salario > 1250:
    nSalario = salario + (salario * 0.10)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, nSalario))
if salario <= 1250:
    nSalario = salario + (salario * 0.15)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, nSalario))