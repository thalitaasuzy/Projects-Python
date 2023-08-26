A=0
E=0
J=int(input('Quantas partidas você deseja jogar?'))
for x in range (1,J+1): 
 P=int(input('Digite um núimero entre 1 e 3: '))
 from random import randint
 N=randint (1,3)
 print ('O NÚMERO SORTEADO É', N)

 if P==N:
  print ('Você acertou!!! Parabéns!!!')
  A=A+1
 else:
  print ('Tente outra vez...')
  E=E+1
  
print ('Você acertou', A,'vezes')
print ('Você errou', E,'vezes')

PA=A/J * 100
PE=E/J * 100

print ('O percentual de acertos foi', PA,'%')
print ('O percentual de erros foi', PE,'%')

if A>=3:
  print ('Você ganhou do computador!!!')
else:
  print ('Você perdeu para o computador.')