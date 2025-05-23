n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
# Verificando o menor número
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
# Verificando o maior número
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
# printando o resultado
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
# Outra forma de fazer
'''if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}')

elif n1 <= n2 and n1 <= n3:
    print(f'O menor número é{n1}')
elif(n2 <= n1 and n2 <= n3):
    print(f'O menor número é {n2}')
elif(n3 <= n1 and n3 <= n2):
    print(f'O menor número é {n3}')

elif n1 == n2 and n1 == n3:
    print('Os três número são iguais')'''
