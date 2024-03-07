from datetime import date
ano = int(input('Ano de nascimento: '))
Yatual = date.today().year
idade = Yatual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, Yatual))
if idade < 18:
    print('Ainda falta {} anos para seu alistamento'.format(18-idade))
    print('Seu alistamento será em {}'.format(ano+18))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade-18))
    print('Seu alistamento foi em {}'.format(ano+18))
else:
    print('Você tem que se alistar esse ano')

