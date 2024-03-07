gols = list()
time = list()
dados = dict()
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    gols.clear()
    for i in range(1, jogos + 1):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    time.append(dados.copy())
    while True:
        op = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if op in 'SN':
            break
        print('ERRO! Digite somente S ou N')
    if op != 'S':
        break
print(30*'—=')
print('cod', end=' ')
for i in dados.keys():
    print(f'{i:<15}', end=' ')
print()
print(30*'—')
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar os dados de qual jogador (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! nao existe jogado com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, v in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i+1} fez {v} gols')
    print('—'*40)



