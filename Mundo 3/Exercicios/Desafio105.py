def notas(*notas, sit=False):
    """
    ---> Função para analisar notas e situações de vários alunos
    :param notas: Uma ou mais notas dos alunos
    :param sit: (Opcional) Indica se deve ou não conter a situação
    :return: Dicionário com as estatísticas sobre as notas
    """
    t = m = 0
    n = dict()
    for i, v in enumerate(notas):
        t += v
    m = t / len(notas)
    n['Total'] = len(notas)
    n['Maior'] = max(notas)
    n['Menor'] = min(notas)
    n['Média'] = f'{m:.1f}'
    if sit:
        if m >= 7:
            n['Situação'] = 'BOA'
        elif m <= 4:
            n['Situação'] = 'RUIM'
        else:
            n['Situação'] = 'RAZOÁVEL'
    return n


help(notas)
r = notas(5.5, 9.5, 10, 6.5, sit=True)
print(r)
