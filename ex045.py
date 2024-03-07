print('Gerador de PA')
print(8*'—=')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA:'))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end=' ')
        termo = termo + r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))  
print('Progressão finalizada com {} tantos termos mostrados'.format(total))