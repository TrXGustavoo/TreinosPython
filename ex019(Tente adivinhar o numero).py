import random
from time import sleep
print('—=—' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('—=—' * 20)
n = random.randint(0,5) #Faz o computador escolher um numero
resposta = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if resposta == n:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(n,resposta))