S = float(input('Qual é a distancia da sua viagem? '))
if S <= 200:
    Pp = 0.50 * S
    print('E o preço da sua passagem será de {}'.format(Pp))
else:
    Pp = 0.45 * S
    print('E o preço da sua passagem será de {}'.format(Pp))