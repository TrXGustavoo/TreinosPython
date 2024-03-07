from dataclasses import replace
def dobro(preco, f=False):
    res = preco * 2
    if f:
        return moeda(res)
    else:
        return res


def metade(preco,f=False):
    res = preco/2
    if f:
        return moeda(res)
    else:
        return res



def aumentar(preco=0, taxa=0, taxaR=0, f=False):
    res =  preco + (preco * taxa/100)
    if f:
        return moeda(res)
    else:
        return res


def diminuir(preco=0, taxa=0, taxaR=0, f=False):
    res =  preco - (preco * taxa/100)
    if f:
        return moeda(res)
    else:
        return res


def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, taxa=0, taxaR=0, f=False):
    print(f'—'*30)
    print('RESUMO DO VALOR'.center(30))
    print(f'—'*30)
    print(f'Preço analisado: {moeda(preco).center(15)}')
    print(f'Dobro do preço: {dobro(preco,f).center(15)}')
    print(f'Metade do preço: {metade(preco,f).center(15)}')
    print(f'{taxa}% de aumento: {aumentar(preco,taxa,taxaR,f).center(15)}')
    print(f'{taxaR}% de redução: {diminuir(preco,taxa,taxaR,f).center(15)}')
    print(f'—'*30)

