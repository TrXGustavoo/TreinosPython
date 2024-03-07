geral = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        geral[0].append(n)
    else:
        geral[1].append(n)
print(30*'—=')
geral[0].sort()
geral[1].sort()
print(f'Os valores pares digitados foram: {geral[0]}')
print(f'Os valores impares digitados foram: {geral[1]}')
