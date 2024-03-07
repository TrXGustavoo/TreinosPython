n = (int(input('Digite um número: ')), 
    int(input('Digite outro número: ')), 
    int(input('Digite mais um número: ')), 
    int(input('Digite um  ultimo número: ')))
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro numero 3 esta na posição {n.index(3)+1}')
else:
    print('Não há valor 3')
for i in n:
    if i % 2 == 0:
        print(i, end='  ')