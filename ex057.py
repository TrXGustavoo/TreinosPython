from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), 
    randint(1, 10), randint(1, 10))
print(f'Sorteei os valores foram: ')
for i in n:
    print(f'{i} ', end=' ')
print(f'\nO maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
