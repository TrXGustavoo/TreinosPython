gols = list()
dados = {'Nome': str(input('Nome do Jogador: ')),
         'Gols': gols}
jogos = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for i in range(1, jogos+1):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    dados['Total'] = sum(gols)
print(30*'—=')
print(dados)
print(30*'—=')
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print(30*'—=')
print(f'O jogador {dados["Nome"]} jogou {jogos} partidas')
for kk, vv in enumerate(gols):
    print(f' => Na partida {kk+1}, fez {vv} gols')
print(f'Foi um total de {dados["Total"]} gols')
