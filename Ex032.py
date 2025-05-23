from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto!\n Ou digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')