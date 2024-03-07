pessoas = []
dadosT = []
maior = menor = 0
while True:
    dadosT.append(str(input('Nome: ')))
    dadosT.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dadosT[1]
    else:
        if dadosT[1] > maior:
            maior = dadosT[1]
        if dadosT[1] < menor:
            menor = dadosT[1]
    pessoas.append(dadosT[:])
    dadosT.clear()
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(30*'—=')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas', )
print(f'O maior peso foi de {maior}kg. Peso de ',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg. Peso de ',end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
