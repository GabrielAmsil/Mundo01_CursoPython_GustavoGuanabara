num = 'Escolha um numero entre 0 e 9999'
print(num)
num = int(input('Digite um numero: '))
print(f'Analisando o numero {num}')
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
print('Fim do progama')