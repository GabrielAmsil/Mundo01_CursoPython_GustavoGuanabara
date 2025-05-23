nome = str(input('Digite seu nome completo: ')).strip()
print(f'Vamos ver seu primeiro e ultimo nome')
n = nome.split()
print(f'Seu primeiro nome é {n[0]} e seu ultimo nome é {n[-1]}')