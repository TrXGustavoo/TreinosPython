
print(30*'—')
print('    LOJA SUPER BARATÃO    ')
print(30*'—')
nome = str(input('Nome do Produto: '))
valor = float(input('Preço: R$'))
total = valor
cont = 0
nomeB  = nome
valorB = valor
while True:
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    if op == 'N':
        break
    nome = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$'))
    if valor > 1000:
        cont += 1
    total += valor
    if valor < valorB:
        valoB = valor
        nomeB = nome

print('     FIM DO PROGRAMA    ')
print(f'O total da compra foi R${total:.2f} ')
print(f'Temos {cont} produtos custando mais de R$1000.00 ')
print(f'O produto mais barato foi {nomeB} que custa R${valorB}')
