from time import sleep


def maior(lista):
    print('—='*30)
    print('Analisando o valores passados...')
    for j in n:
        print(j, end=' ')
        sleep(0.4)
    print(f'Foram informados {len(n)} valores ao todo')
    m = 0
    for i in range(0, 2):
        if lista[i] > m:
            m = lista[i]
    print(f'O maior valor informado foi {m}')


n = [2, 9, 4, 5, 7, 1]
maior(n)
n = [4, 7, 0]
maior(n)
n = [1, 2]
maior(n)
n = [6]
maior(n)
n = []
maior(n)

#Segunda solução


# def maior(*num):
#     cont = m = 0
#     print('—='*30)
#     print('Analisando o valores passados...')
#     for j in num:
#         print(j, end=' ')
#         sleep(0.4)
#         if cont == 0:
#             m = j
#         else:
#             if j > m:
#                 m = j
#         cont += 1
#     print(f'Foram informados {len(num)} valores ao todo')
#     print(f'O maior valor informado foi {m}')
#
#
# n = (2, 9, 4, 5, 7, 1)
# maior(n)
# n = (4, 7, 0)
# maior(n)
# n = (1, 2)
# maior(n)
# n = 6
# maior(n)
# n = ()
# maior(n)
#
#
