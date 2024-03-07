from time import sleep


def menu():
    print('—'*30)
    print(f'MENU PRINCIPAL'.center(30))
    print('—'*30)
    print(f'1 — Ver pessoas cadastradas\n2 — Cadastrar uma nova pessoa\n3 — Sair do programa')


def op(msg):
    while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print('Erro por favor informe um numero inteiro valido')
            else:
                if n == 1:
                    esc(n)
                    break
                elif n == 2:
                    esc(n)
                    break
                elif n == 3:
                    esc(n)
                    break
                else:
                    print(f'ERRO! Opção invalida ')
                    menu()


def esc(n):
    if n == 1:
        print('—'*30)
        print(f'OPÇÃO 1'.center(30))
        print('—'*30)
        sleep(2)
        menu()
        op('Sua opção: ')
    if n == 2:
        print('—'*30)
        print(f'OPÇÃO 2'.center(30))
        print('—'*30)
    if n == 3:
        print('—'*30)
        print(f'Saindo do sistema... Até logo!'.center(30))
        print('—'*30)
     
     
        