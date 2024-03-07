pessoa = dict()
bd = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    bd.append(pessoa.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if op in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if op == 'N':
        break
print(30*'—=')
print(f'Ao todo temos {len(bd)} pessoas cadastradas')
media = soma / len(bd)
print(f'A media de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: ', end=' ')
for p in bd:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end=' ')
print()
print(f'Lista das pessoas que estao acima da media: ')
for p in bd:
    if p['Idade'] >= media:
        print(f'      ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
        