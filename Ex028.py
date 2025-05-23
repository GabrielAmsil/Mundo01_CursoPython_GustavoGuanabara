'''u = int(input('Olá usuário, digite qualquer número entre um e cinco:'))
if u == 1:
    print('Você digitou o número um!')
elif u == 2:
    print('Você digitou o número dois!')
elif u == 3:
    print('Você digitou o número três!')
elif u == 4:
    print('Você digitou o número quatro!')
elif u == 5:
    print('Você digitou o número cinco!')
else:
    print('Você não digitou um número entre um e cinco!')
print('Fim do programa!')'''

import emoji
from time import sleep
from random import randint

print(24 * '=-')
print('Tenta adivinha o número que eu vou escolher! 😊')
print(24 * '=-')

Jogador = int(input('Chute um número entre 0 e 5: ')) # O jogador tenta adivinhar o número
computador = randint(0, 5) # Faz o computador "pensar"
print('Processando...')
sleep(2)

print('Eu escolhi o número {}.'.format(computador))

if Jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('\033[0;30;35m Você Errou Que peninha 😂\033[m{}.'.format(computador))
    print('tente de novo! 😉')