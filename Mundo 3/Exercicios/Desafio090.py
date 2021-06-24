aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 7 > aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=-' * 49)
print(f'Nome: {aluno["nome"]}\nMédia: {aluno["média"]}\nSituação: {aluno["situação"]}')
print('-=-' * 49)
