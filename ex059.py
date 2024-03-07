print(40*'—')
print('{:^30}'.format('LISTAGEM DE PREÇO'))
print(40*'—')
produtos = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for i in range(0, len(produtos)):
    if i % 2 == 0: 
        print(f'{produtos[i]:.<30}', end=' ')
    else:
        print(f'R${produtos[i]:>7.2f}')
print(40*'—')

