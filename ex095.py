def leiaint(msg):
    ok = False
    valor = 0
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('Erro por favor informe um numero inteiro valido')
        except KeyboardInterrupt:
            print('\nErro por favor informe um numero inteiro valido')
        else:
            return inteiro


def leiafloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('Erro por favor informe um numero inteiro valido')
        except KeyboardInterrupt:
            print('Erro por favor informe um numero inteiro valido')
        else:
            break
    return real


Inteiro = leiaint('Digite um número Inteiro: ')
Real = leiafloat('Digite um número Real: ')

print(f'Você acabou de digitar o número inteiro {Inteiro} e o numero real {Real}')
