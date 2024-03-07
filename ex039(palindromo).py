from operator import inv


frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
# for i in range(len(junto) -1, -1, -1):
#    inverso += junto[i]
if inverso == junto:
    print('Temos um palindromo') 
else:
    print('A frase digitada não é um palíndromo!')
print(junto, inverso)