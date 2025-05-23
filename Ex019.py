from random import choice
A1 = str(input('Primeiro aluno:'))
A2 = str(input('Segundo aluno:'))
A3 = str(input('Terceiro aluno:'))
A4 = str(input('Quarto aluno:'))
alunos = [A1, A2, A3, A4]
escolhido = choice(alunos)
print('O aluno escolhido foi {}'.format(escolhido))
