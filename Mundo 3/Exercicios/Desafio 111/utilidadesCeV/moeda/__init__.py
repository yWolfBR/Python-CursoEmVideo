def aumentar(v=0, t=0, formatar=False):
    vf = v + (v * (t / 100))
    if formatar:
        vf = moeda(vf)
    return vf


def diminuir(v=0, t=0, formatar=False):
    vf = v - (v * (t / 100))
    if formatar:
        vf = moeda(vf)
    return vf


def dobro(v=0, formatar=False):
    vf = v * 2
    if formatar:
        vf = moeda(vf)
    return vf


def metade(v=0, formatar=False):
    vf = v / 2
    if formatar:
        vf = moeda(vf)
    return vf


def moeda(v=0.0, m='R$'):
    vf = f'{m}{v:.2f}'.replace('.', ',')
    return vf


def resumo(v=0, t1=0, t2=0):
    print(f'''{"-" * 35}
          RESUMO DO VALOR          
{"-" * 35}
Preço Analisado:{moeda(v):>19}
Dobro do Preço:{dobro(v, True):>20}
Metade do Preço:{metade(v, True):>19}
{str(t1) + "%":<4} de aumento:{aumentar(v, t1, True):>19}
{str(t2) + "%":<4} de redução:{diminuir(v, t2, True):>19}
{"-" * 35}''')
