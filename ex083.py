import random
from time import sleep

numeros = list()


def sorteia(lista):
    for i in range(0, 5):
        lista.append(random.randint(1, 10))
    print('Sorteando 5 valores da lista:', end=' ')
    for j in range(0, 5):
        print(f'{numeros[j]}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar():
    soma = 0
    for k in numeros:
        if k % 2 == 0:
            soma += k
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia(numeros)
somaPar()

