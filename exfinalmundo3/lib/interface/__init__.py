def linha(tam=42):
    return '—'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('Erro por favor informe um numero inteiro valido')
        else:
            return inteiro
     
     
        