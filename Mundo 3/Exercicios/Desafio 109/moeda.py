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
