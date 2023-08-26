#Números Aleatórios (case 2)

from random import randint 

N = randint(1,3)
JOGADAS = int(input('Quantas partidas você quer jogar??? '))
a = 0
ACERTOS = 0
ERROS = 0


while a < JOGADAS:
  X = int(input('Digite um número aleátorio entre 1 e 3: '))
  if X != N:
    print ('VocÊ errou, tente outra vez!!')
    ERROS = ERROS + 1
  if X == N: 
    print ('VocÊ acertou!!!!!')
    ACERTOS = ACERTOS + 1
  a = a + 1
print ('O seu percentual de acertos foi: ', ACERTOS/5 * 100, '%')
print ('O seu percentual de erros foi: ', ERROS/5 * 100, '%')

if ACERTOS/5 * 100 > 50.0:
  print ('VocÊ ganhou o jogo!!!!!')
if ACERTOS/5 * 100 < 50.0:
  print ('VocÊ perdeu o jogo!!!!!')