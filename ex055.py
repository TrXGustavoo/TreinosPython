cont = (0, 1, 2, 3, 4, 
        5, 6, 7, 8, 9, 
        10, 11, 12, 13, 14, 
        15, 16, 17, 18, 
        19, 20)
while True:        
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        print('Tente novamente. ', end=' ')
        n = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {cont[n]}')
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
