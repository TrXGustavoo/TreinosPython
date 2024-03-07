import random
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
pc = random.randrange(0,11)
x = int(input('Qual é seu palpite? '))
cont = 0
while x != pc:
    if x > pc:
        print('Menos... Tente mais uma vez')
        x = int(input('Qual é seu palpite? '))
    elif x < pc:
        print('Mais... Tente mais uma vez')
        x = int(input('Qual é seu palpite? '))
    cont += 1
print('Acertou com {} tentativas. Parabéns'.format(cont + 1))
