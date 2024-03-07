# 1º solução 
num = []
pares = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        if n == 0:
            num.append(n)
        else:
            num.append(n)
            pares.append(n)
    elif n % 2 != 0:
        num.append(n)
        impar.append(n)
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
num.sort()
pares.sort()
impar.sort()
print('—='*30)
print(f'Lista com todos os valores: {num}')
print(f'Lista com somente os valores pares: {pares}')
print(f'Lista com somente os valores impares: {impar}')

#2º solução
# num = []
# pares = []
# impar = []
# while True:
#     num.append(int(input('Digite um valor: ')))
#     op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#     if op == 'N':
#         break
# for i, v in enumerate(num):
#     if v % 2 == 0:
#         if v == 0:
#             c = 0
#         else:    
#             pares.append(v)
#     else:
#         impar.append(v)
# num.sort()
# pares.sort()
# impar.sort()
# print('—='*30)
# print(f'Lista com todos os valores: {num}')
# print(f'Lista com somente os valores pares: {pares}')
# print(f'Lista com somente os valores impares: {impar}')