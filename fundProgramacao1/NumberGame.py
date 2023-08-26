#Geração de números aleatórios, o computador vai gerar um número aleátorio de N (entre um valor mínimo e max), e o player vai chutar que número (x) seria esse. A diferença entre o número N e x (N-x) é a quantidade de pontos que o player acumula. A quantidade de rodadas e a jogadores pode ser escolhida pelo usuário. Quem acumular menos pontos ganha.


from random import randint 

#1 parte: escolher jogadores

player1 = input ('Player 1, digite um nick: ')
print ('SEU NICKNAME É' , player1)

player2 = input ('Player 2, digite um nick: ')
print ('SEU NICKNAME É ', player2)

#2 parte: quantidade de rodadas
rodadas = input('Determine a quantidade de rodadas: ')

#3 parte: Computador escolhe n~umero aleatório

N = randint (1,10)

print ('O computador vai escolher um número aleátorio entre 1 e 50...')
print ('.')
print ('.')
print ('.')
print ('O número foi escolhido =)) 🙅🏻😜')

#4 players escolhem um n~umero
print ('Player 1: É a sua vez!!!!!🎊🎉')
Answer1 = int(input('Digite o número que você acha que o computador escolheu: '))

print ('Player 2: Sua vez de mostrar para que cê veio💪🏽👊🏽')
Answer2 = int(input('Digite o número que você acha que o computador escolheu: '))

#5 computador revela a resposta
print (N)