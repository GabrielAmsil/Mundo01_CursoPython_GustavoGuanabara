'''co = float(input('Qual é o comprimento do cateto oposto? '))
ca = float(input('Qual é o comprimento do cateto adjecente? '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

from math import hypot
co = float(input('Qual é o comprimento do cateto oposto? '))
ca = float(input('Qual é o comprimento do cateto adjacente? '))
hipotenusa = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
