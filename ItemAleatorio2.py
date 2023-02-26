# >>> choice(['win', 'lose', 'draw'])      # Single random element from a sequence
# 'draw'

from random import choice
n1 = input('Digite o nome do primeiro aluno: ' )
n2 = input('Digite o nome do segundo aluno: ' )
n3 = input('Digite o nome do terceiro aluno: ' )
n4 = input('Digite o nome do quarto aluno: ' )

Lista = [n1,n2,n3,n4]
AlunoEscolhido = choice(Lista)
print (f'O alun@ escolhid@ é {AlunoEscolhido} ')
