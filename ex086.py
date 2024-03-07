def fatorial(n, s=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param s: (opcional) Mostrar ou nao a conta
    :return: o valor do Fatorial de um numero n
    """
    if s:
        print(f'{n} x', end=' ')
    for i in range(n - 1, 0, -1):
        if s:
            if i != 1:
                print(f'{i} x', end=' ')
            else:
                print(f'{i} =', end=' ')
        n *= i
    return n


f = int(input('Digite um numero para calcular se fatorial: '))
op = str(input('Deseja ver a conta: [Sim/Nao]')).upper().strip()[0]
if op == 'S':
    op = True
else:
    op = False
print(fatorial(f, op))


