preço = float(input('Digite o preço do produto: R$'))
desconto = 20
preço_final = preço - (preço * desconto / 100)
print('O preço do produto com desconto de {}% é R${:.2f}'.format(desconto, preço_final))
