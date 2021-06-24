from datetime import datetime

t = dict()
t['nome'] = str(input('Nome: ')).strip().capitalize()
t['idade'] = datetime.today().year - int(input('Ano de Nascimento: '))
t['ctps'] = int(input('Carteira de Trabalho - (0 Caso não possua): '))
if t['ctps'] > 0:
    t['contratação'] = int(input('Ano de Contratação: '))
    t['salário'] = float(input('Salário: R$'))
    t['aposentadoria'] = t['idade'] + ((t['contratação'] + 35) - datetime.today().year)

print('-=-' * 49)
for k, v in t.items():
    print(f'{k.capitalize()}: {v}')
