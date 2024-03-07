print(15*'—')
print('Sequência de Fibonacci')
print(15*'—')
n = int(input('Quantos termos você quer mostrar?' ))
cont = 2
t1 = 0
t2 = 1
t3 = 0
print('{}'.format( t2),end=' ')
while cont <= n:
    t3 = t1 + t2
    print('{}'.format(t3),end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
