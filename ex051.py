import random
print(10*'=-')
print('VAMOS JOGAR PAR OU IMPAR')
print(10*'=-')
nP = int(input('Diga um valor: '))
nC = random.randint(1,10)
print(nC)
PI = str(input('Par ou impar? ')).upper().strip()[0]
cont = 0
while True:
    if PI == 'P':
        if (nP + nC) % 2 == 0:
            print(20*'—')
            print(f'Você jogou {nP} e o computador {nC}. Total de {nP+nC} DEU PAR')
            print(20*'—')
            print('Voce VENCEU\nVamos jogar novamente...')
            print(10*'=-')
            cont += 1
        elif (nP + nC) % 2 != 0:
            print(20*'—')
            print(f'Você jogou {nP} e o computador {nC}. Total de {nP+nC} DEU IMPAR')
            print(20*'—')
            print('Voce PERDEU')
            print(10*'=-')
            break
    if PI == 'I':
        if (nP + nC) % 2 != 0:
            print(20*'—')
            print(f'Você jogou {nP} e o computador {nC}. Total de {nP+nC} DEU PAR')
            print(20*'—')
            print('Voce VENCEU\nVamos jogar novamente...')
            print(10*'=-')
            cont += 1
        elif (nP + nC) % 2 == 0:
            print(20*'—')
            print(f'Você jogou {nP} e o computador {nC}. Total de {nP+nC} DEU IMPAR')
            print(20*'—')
            print('Voce PERDEU')
            print(10*'=-')
            break
    nP = int(input('Diga um valor: '))
    #escolher um numero para o bot
    nC = random.randint(1,10)
    # print(nC)
    PI = str(input('Par ou impar? ')).upper().strip()[0]
print(f'GAME OVER! Você venceu {cont} vezes.')

