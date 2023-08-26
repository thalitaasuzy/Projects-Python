
qtd1= qtd2 =qtd3= 0

import random
 
res = [random.randrange(0, 10, 1) for i in range(50)]
 
print (str(res))

for x in res: 
  if x == 1: qtd1 = qtd1 + 1
  if x == 2: qtd2 = qtd2 + 1
  if x == 3: qtd3 = qtd3 + 1

print ("O número 1 aparece = " , qtd1," vzs" )
print ("O número 2 aparece = " , qtd2," vzs" )
print ("O número 3 aparece = " , qtd3," vzs" )

if qtd1>qtd2 and qtd1>qtd3 :
  print ('O número 1 aparece mais vezes')
if qtd2>qtd1 and qtd2>qtd3:
  print ('O número 2 aparece mais vezes')
if qtd3>qtd1 and qtd3>qtd2:
  print ('O número 3 aparece mais vezes')
if qtd1==qtd2 and qtd1>qtd3:
  print ('Os números 1 e 2 aparecem mais que 3, e aparecem na mesma quantidade')
if qtd1==qtd3 and qtd1>qtd2:
  print ('Os números 1 e 3 aparecem mais que 2, e aparecem na mesma quantidade')
if qtd2==qtd3 and qtd2>qtd1:
  print ('Os números 2 e 3 aparecem mais que 1, e aparecem na mesma quantidade')




