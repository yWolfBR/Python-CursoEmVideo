from math import radians, sin, cos, tan

a = float(input('Digite o ângulo: '))
print('O ângulo de {} tem, respectivamente:\nSENO de {:.2f}\nCOSSENO de {:.2f}\nTANGENTE de {:.2f}'
      .format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
