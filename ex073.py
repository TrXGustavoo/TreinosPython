geral = dict()
geral['nome'] = str(input('Nome:'))
geral['Media'] = float(input(f'Média de {geral["nome"]}: '))
if 6 <= geral['Media'] < 7:
    geral['situação'] = 'Recuperação'
elif geral['Media'] < 6:
    geral['situação'] = 'Reprovado'
else:
    geral['situação'] = 'Aprovado'
for i, j in geral.items():
    print(f'{i} é igual a {j}')


