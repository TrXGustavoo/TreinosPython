num = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista')
    else: 
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'os valores digitados em ordem foram {num}')    
