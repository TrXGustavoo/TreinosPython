from ntpath import join


def leiaDinheiro(msg):
    valido = False
    while not valido:
        ventrada = str(input(msg)).replace(',','.').strip().split()
        entrada = ''.join(ventrada)
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \"{ventrada}\" é um preço invalido')
        else:
            valido = True
            return float(entrada)