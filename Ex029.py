carro = float(input('Qual a velocidade do carro? '))
if carro > 80:
    print('Você ultrapassou a velocidade permitida de 80km/h')
multa = (carro - 80) * 7
if multa > 0:
    print(f'Você pagará uma multa de R${multa:.2f}')
else:
    print('Você está dentro do limite de velocidade')
        