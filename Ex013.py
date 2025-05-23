salário = float(input('Qual o slário do funcionário? R$'))
aumento = 15
salário_final = salário + (salário * aumento / 100)
print('O salário do funcionário com aumento de {}% é R${:.2f}'.format(aumento, salário_final))
