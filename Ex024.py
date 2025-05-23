cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(f'A cidade {cidade} começa com a letra "RIO"?')
print(cidade[:4].upper() == 'RIO')