def medidas(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m²')


print('Controle de Terrenos')
print('—'*20)
medidas(float(input('LARGURA(M): ')), float(input('COMPRIMENTO(M): ')))
