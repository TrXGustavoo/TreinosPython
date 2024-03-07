#Primeira solução
from time import sleep


def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        for i in range(a, b+1, c):
            print(i, end=' ')
            sleep(0.4)
        print('FIM!')
    elif a > b:
        if c > 0:
            c = c * -1
        for i in range(a, b-1, c):
            print(i, end=' ')
            sleep(0.4)
        print('FIM!')
    print('—=' * 30)


print(30*'—=')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim:')), int(input('Passo: ')))

#Segunda solução


# def contador(i, f, p):
#     print(f'Contagem de {i} até {f} de {p} em {p}')
#     sleep(2.5)
#
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end=' ')
#             sleep(0.5)
#             cont += p
#         print('FIM!')
#         print(20 * '—=')
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end=' ')
#             sleep(0.5)
#             cont -= p
#         print('FIM!')
#         print(20 * '—=')
#
#
# print('—='*20)
# contador(1, 10, 1)
# contador(10, 0, 2)
# contador(int(input('Inicio: ')), int(input('Fim:')), int(input('Passo: ')))
