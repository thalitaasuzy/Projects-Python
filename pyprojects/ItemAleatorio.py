#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import randint
n1 = input('Digite o nome do primeiro aluno: ' )
n2 = input('Digite o nome do segundo aluno: ' )
n3 = input('Digite o nome do terceiro aluno: ' )
n4 = input('Digite o nome do quarto aluno: ' )

chosed = randint(1, 4 + 1)
if chosed == 1:
    print(f' O aluno(a) escolhido(a) é {n1}')
if chosed == 2:
    print(f'O aluno(a) escolhido(a) é {n2}')
if chosed == 3:
    print(f'O aluno(a) escolhido(a) é {n3}')
if chosed == 4:
    print(f'O aluno(a) escolhido(a) é {n4}')

