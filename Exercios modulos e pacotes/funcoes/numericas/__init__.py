def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3



def metade(n):
    res = n/2
    return res


def aumentar(n, taxa):
    res =  n + (n* taxa/100)


def dimunuir(n, taxa):
    res =  n - (n* taxa/100)
