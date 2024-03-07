cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vemelho': '\033[31m',
         'verde': '\033[32m'}
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('{}{}{} é um número par'.format(cores['azul'], n, cores['limpa']))
else:
    print('{}{}{} é um número impar'.format(cores['verde'], n, cores['limpa']))
