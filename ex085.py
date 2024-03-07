import datetime
from datetime import date


def voto(ano):
    global idade
    idade = datetime.datetime.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


idade = 0
print(voto(int(input('Ano de nascimento: '))))

