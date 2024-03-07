from exfinalmundo3.lib.interface import *
from exfinalmundo3.lib.arquivo import *
from time import sleep


arq = 'banco.txt'

if not arqExiste(arq):
    criararquivo(arq)

while  True:
    resposta = menu(['[1]Ver pessoas cadastradas', '[2]Cadastrar uma nova pessoa', '[3]Sair do programa' ])
    if resposta == 1:
        # Opção de listar o conteudo do txt
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m') 
    sleep(0.5)   
