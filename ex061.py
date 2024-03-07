n = []
maior = menor = 0
for i in range(0, 5):
    n.append(int(input(f'Digite um valor para a Posição {i}: ')))
    if i == 0:
        maior = menor = n[i]
    else:
        if n[i] > maior:
            maior = n[i]
        if n[i] < menor:
            menor = n[i]
print(20*'=—')
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {maior} nas posições:', end=' ')
for j , v in enumerate(n):
    if v == maior:
        print(f'{j}...',end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições:', end=' ')
for j , v in enumerate(n):
    if v == menor:
        print(f'{j}...',end=' ')