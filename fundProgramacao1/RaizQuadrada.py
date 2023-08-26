print ('Eu resolvo p/ vc ~~ computador 😉' )

import math
  #raiz quadrada de um número
print ('###Calcular Raiz Quadrada###')
print ('***Para finalizar o calculo, digite 0.') 

a = float(input('Digite um número: '))

if (a!= 0):
   b = math.sqrt(a)
   print ('A raiz de é ', b)
while (a != 0):
    a = float(input('Digite um número: '))
    b = math.sqrt(a)
    print ('A raiz de ',a, 'é ', b)

else:
  if (a == 0):
    print ('VocÊ finalizou o loop', ' 🥳 🎉 🥳 🎉 🥳')

