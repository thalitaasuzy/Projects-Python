#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#deck = 'ace two three four'.split()
#>>> shuffle(deck)                        # Shuffle a list
#>>> deck

import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

#Forma que altera diretamente a lista criada
List = [n1,n2,n3,n4]
random.shuffle(List)
print(List)

#Forma que cria uma nova lista embaralhada a partir da primeira, e que pode ser delimitada (k), fznd com que nem
#todos os itens apareçam.
NewList = random.sample([n1,n2,n3,n4], k=4)
print(NewList)

