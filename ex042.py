n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print("""[1] Soma
[2] Mutiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
op = int(input('Qual é sua opção? '))
while op != 5:
    if op == 1:
        resultado = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, resultado))
        print(10*'=—=')
        print('Escolha uma nova opção')
        print("""[1] Soma\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
        op = int(input('Qual é sua opção? '))
    elif op == 2:
        resultado = n1 * n2
        print('A mutiplicação entre {} * {} é {}'.format(n1, n2, resultado))
        print(10*'=—=')
        print('Escolha uma nova opção')
        print("""[1] Soma\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
        op = int(input('Qual é sua opção? '))
    elif op == 3:
        if n1 > n2:            
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {} '.format(n1, n2, maior))
        print(10*'=—=')
        print('Escolha uma nova opção')
        print("""[1] Soma\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
        op = int(input('Qual é sua opção? '))
    elif op == 4:
        print('Digite os dois valores novos')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(10*'=—=')
        print('Escolha uma nova opção')
        print("""[1] Soma\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
        op = int(input('Qual é sua opção? '))
    else:
        print('Opção invalida')
        print('Escolha uma nova opção')
        print("""[1] Soma\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa""")
        op = int(input('Qual é sua opção? '))
print('Programa encerrado')