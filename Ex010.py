dinheiro = float(input('Digite o valor que você tem na carteira: R$'))
dolar = 5.25
euro = 5.50
d = dinheiro / dolar
e = dinheiro / euro
print('Com R${:.2f} você pode comprar US${:.2f} e pode comprar E${:.2f}'.format(dinheiro, d, e))

