from datetime import date
trabalhador = {'Nome': str(input('Nome: ')),
               'idade': date.today().year - int(input('Ano de nascimento: ')),
               'CTPS': int(input('Carteira de trabalho (0 não tem): '))}
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = int(input('Salário: R$'))
    trabalhador['Aposentadoria'] = trabalhador['idade'] + ((trabalhador['Ano de Contratação'] + 35) - date.today().year)
print(30*'—=')
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
