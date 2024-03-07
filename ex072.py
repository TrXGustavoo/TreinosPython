alunoseN = list()
mediaN = list()
media = 0
while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    media = (n1 + n2)/2
    mediaN.append([nome, [n1, n2], media])
    alunoseN.clear()
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(30*'—=')
print(f'{"No.":<4}{"Nome":10}{"MÉDIA":>9}')
print(25*'—')
for i, j in enumerate(mediaN):
    print(f'{i:<4}{j[0]:<10}{j[2]:>8.1f}')
print(25*'—')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interompe) '))
    if opc == 999:
        break
    if opc <= len(mediaN) - 1:
        print(f'As notas de {mediaN[opc][0]} foram: {mediaN[opc][1]}')
   