sal = float(input('Qual o salário do funcionário? R$'))
if sal <= 1250:
    aumento = sal * 0.15
if sal > 1250:
    aumento = sal * 0.10
    novo_sal = sal + aumento
novo_sal = sal + aumento
print(f'O novo salário do funcionário é R${novo_sal}')