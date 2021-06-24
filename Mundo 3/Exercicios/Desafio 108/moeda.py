def aumentar(v=0, t=0):
    vf = v + (v * (t / 100))
    return vf


def diminuir(v=0, t=0):
    vf = v - (v * (t / 100))
    return vf


def dobro(v=0):
    vf = v * 2
    return vf


def metade(v=0):
    vf = v / 2
    return vf


def moeda(v=0, m='R$'):
    vf = f'{m}{v:.2f}'.replace('.', ',')
    return vf
