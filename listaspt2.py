teste = list()
teste.append('Gustavo')
teste.append(40)
pessoas = list()
pessoas.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
print(teste)
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
