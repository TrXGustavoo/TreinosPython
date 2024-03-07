# print(24*'—')
# print('   CADASTRE UMA PESSOA   ')
# print(24*'—')
# idade = int(input('Idade: '))
# sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
# print(24*'—')
cont18 = contm = contf = 0
r = 'S'
while True:
    if r == 'N':
        break
    print(24*'—')
    print('   CADASTRE UMA PESSOA   ')
    print(24*'—')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print(24*'—')
    if idade  >= 18:
        cont18 += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F':
        if idade < 20:
            contf += 1

print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {contm} homens cadastrados')
print(f'E {contf} mulheres com menos de 20 anos')

