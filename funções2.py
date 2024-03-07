def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio do da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c += p
    print('FIM!')


help(contador)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


print(somar(3, 2, 5))
somar(2, 2)
r1 = somar(4)
print(f'{r1}')


n = 2


def teste():
    global n
    n = 4
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


teste()
print(f'No programa principal n vale {n}')
# print(f'No programa principal x vale {x}') isso nao funciona x é uma variavel local



