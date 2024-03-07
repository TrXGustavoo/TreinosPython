peso = float(input('Qual seu peso?KG '))
altura = float(input('Qual sua altura?CM  '))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print('O seu IMC é de {:.2f}\nVocê está Abaixo do peso'.format(IMC))
elif 18.5 <= IMC < 25:
    print('O seu IMC é de {:.2f}\nVocê está no Peso ideal'.format(IMC))
elif 25 <= IMC < 30:
    print('O seu IMC é de {:.2f}\nVocê está no Sobrepeso'.format(IMC))
elif 30 <= IMC < 40:
    print('O seu IMC é de {:.2f}\nVocê está no Obesidade'.format(IMC))
elif IMC >= 40:
    print('O seu IMC é de {:.2f}\nVocê está em Obesidade Mórbida'.format(IMC))
