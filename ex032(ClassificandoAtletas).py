from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos.\nClassificação: MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos.\nClassificação: INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos.\nClassificação: JÚNIOR'.format(idade))
elif 19 < idade <= 25:
    print('O atleta tem {} anos.\nClassificação: SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos.\nClassificação: MASTER'.format(idade))

