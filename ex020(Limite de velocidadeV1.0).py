v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    multa = 7 * (v - 80)
    print('Execesso de velocidade você foi multado e o valor da multa foi de R${}'.format(multa))
    print('Tenha um bom dia dirija com segurança')
else:
    print('Tenha um bom dia dirija com segurança')