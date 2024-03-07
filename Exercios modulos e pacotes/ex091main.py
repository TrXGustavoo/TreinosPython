from funcoes import moeda
preco = int(input('Digite o preço:  R$'))
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'Aumentando em 10% temos R${moeda.aumentar(preco, 10)}')
