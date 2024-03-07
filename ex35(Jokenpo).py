import random
from time import sleep
# Faz o computador escolher um numero
Jpc = random.randrange(0, 3)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
op = int(input('Qual é sua jogada? '))
print('JO')
sleep(1.5)
print('KEN')
sleep(1.5)
print('PO!!!')
if Jpc == 0:
    Jpc = 'PEDRA'
    if op == 0:
        op = 'PEDRA'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('EMPATE')
    elif op == 1:
        op = 'PAPEL'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('JOGADOR VENCE')
    elif op == 2:
        op = 'TESOURA'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('COMPUTADOR  VENCE')
    else:
        print('Jogada invalida')
if Jpc == 1:
    Jpc = 'PAPEL'
    if op == 0:
        op = 'PEDRA'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('COMPUTADOR  VENCE')
    elif op == 1:
        op = 'PAPEL'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('EMPATE')
    elif op == 2:
        op = 'TESOURA'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida')
if Jpc == 2:
    Jpc = 'TESOURA'
    if op == 0:
        op = 'PEDRA'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('JOGADOR VENCE')
    elif op == 1:
        op = 'PAPEL'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('COMPUTADOR  VENCE')
    elif op == 2:
        op = 'TESOURA'
        print(11*'—=')
        print('Computador jogou {}\nJogador jogou {}'.format(Jpc, op))
        print(11*'—=')
        print('EMPATE')
    else:
        print('Jogada invalida')
