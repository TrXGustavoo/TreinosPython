sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input("Dados invalidos. Por favor, informe seu sexo: ")).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))