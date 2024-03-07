num = [2, 5, 9, 1]
num[2] = 3
#Adiciona um novo valor
num.append(7)
num.sort(reverse=True)
#Tambem acioniona um novo valor
num.insert(2,0)
#Remove o ultimo valor
num.pop()
#Remove o calor na casa 2
num.pop(2)
#Remove o valor  3 
num.remove(3)
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor')))
for c, i in enumerate(valores):
    print(f'Na posição {c + 1} {i}!')
print('Cheguei ao final da lista')
a =[2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
