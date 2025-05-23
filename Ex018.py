from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que vocÊ deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(a, t))