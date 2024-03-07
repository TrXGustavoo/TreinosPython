s = float(input("Qual é o salario do Funcionario? R$"))
aum = int(input("Porcentagem de de aumento: "))
ns = s + (s * (aum/100))
print("Um funcionario que ganhava R${} com {}% de aumento, passa a recebeer R${:.2f}".format(s, aum, ns))
