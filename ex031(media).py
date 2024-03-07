n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3)/3
if media > 7:
    print('A media desse aluno é igual a {} sendo assim o aluno esta \033[32mAPROVADO\033[m'.format(media))
elif 7 > media >= 5:
    print('A media desse aluno é igual a {} sendo assim o aluno esta de \033[33mRECUPERAÇÃO\033[m'.format(media))
else:
    print('A media desse aluno é igual a {:.2f} sendo assim o aluno esta  \033[31mREPROVADO\033[m'.format(media))