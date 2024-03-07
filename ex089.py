def notas(*num):
    soma = sum(num)
    c = {'Total': len(num)}
    maior = 0
    for i in range(0, len(num)):
        print(i)
        if i == 0:
            menor = num[i]
        if i < menor:
            menor = num[i]
        if i > maior:
            maior = num[i]
    c['Maior'] = maior
    c['Menor'] = menor
    c['Media'] = soma/len(num)
    if c['Media'] < 5:
        sit = 'RUIM'
    elif 5 < c['Media'] < 7:
        sit = 'Boa'
    else:
        sit = 'Otima'
    c['situação'] = sit
    return c


resp = notas(5.5, 2.5, 1.5)
print(resp)
