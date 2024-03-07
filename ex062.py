#1º solução 
num = []
c = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    else:   
        print('Valor duplicado não vou adicionar...')
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
num.sort()
print(f'Você digitou os valores {num}')