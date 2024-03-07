def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)


def contador(*num):
    print(num)
    print(f'Recebi os valores {num} e sao ao todo {len(num)} numeros')
    for i in num:
        print(f'{i} ', end='')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lista):
    pos = 0
    while pos < len(list):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
