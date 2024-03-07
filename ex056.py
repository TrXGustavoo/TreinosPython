from time import time


times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
'São Paulo', 'Fluminense', 'Sport Recife',
'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
'Atlético-GO')
print(f'Os 5 primeiros times são: {times[:5]}')
print(f'Os 4 últimos são: {times[16:]}')
print(f'Times em ordem alfabética{sorted(times)}')
print(f'O Chapecoense esta na posicão {times.index("Chapecoense")}')