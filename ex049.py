n = 0
soma = 0
cont= 0
while True:
    n = int(input('Digite um valor (999 para parara): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}')
    