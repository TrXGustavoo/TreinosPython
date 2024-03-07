r = 'S'
cont = media = soma = maior = menor = 0
while r not in 'N':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
media = soma / cont
print('Você digitou {} números a média entre eles é {}\nO maior foi {} e o menor foi {}'.format(cont,media,maior,menor))
    