try:
    a = int(input('NUMERADOR: '))
    b = int(input('DENOMINADOR: '))
    r = a/b

except (ValueError, TypeError):
    print('Tivemos problemas com os tipos de dados')
except ZeroDivisionError:
    print('Nao é possivel dividir por 0')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar dados')
except Exception as erro:
    print(f'O ERRO encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre mt obrigado')
