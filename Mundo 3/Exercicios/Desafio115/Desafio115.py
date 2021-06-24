from cadastro import *

db = 'database.txt'
if fileisreal(db):
    header(f'       Verificando integridade da DATABASE!\n   Arquivo {db} encontrado com sucesso!')
else:
    header(f'       Verificando integridade da DATABASE!\n       Arquivo {db} não encontrado!')
    filebecomereal(db)
while True:
    menu = cmenu(['Listar Pessoas Cadastradas', 'Novo Cadastro', 'Sair do Programa'])
    if menu == 1:
        header('Lista de Pessoas Cadastradas')
        fileread(db)
    elif menu == 2:
        header('Novo Cadastro')
        n = leiastr('Nome: ')
        i = leiaint('Idade: ')
        filewrire(db, n, i)
    elif menu == 3:
        header('Obrigado por utilizar :)')
        exit()
    else:
        print('OPÇÃO INVÁLIDA!')
