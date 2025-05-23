d = float(input('Digite a distância da viagem em km: '))
print('\033[0;33;35mSua viagem de {} vai começar, senta a bunda na cadeira\33[m'.format(d))
if d <= 200:
    print(f'O preço da passagem é R${d * 0.50:.2f}')
else:
    print(f'O preço da passagem é R${d * 0.45:.2f}')
        