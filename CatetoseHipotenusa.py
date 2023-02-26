#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
# Lembrando pitágoras, para calcular a hipotenusa(a) → a² = b² + c² → a = raiz(a²+b²)

import math

CatOpst = float(input('Digite o valor do Cateto Oposto: '))
CatAdj = float(input('Digite o valor do Cateto Adjacente: '))
print ('Para calcular a hipotenusa, podemos usar pitágoras: ')
print (f'{CatOpst}² + {CatAdj}² = Hipotenusa')

#Cálculo
CatOpst_Quadrado = math.pow(CatOpst, 2)
CatAdj_Quadrado = math.pow(CatAdj, 2)
Hipotenusa = math.sqrt(CatOpst_Quadrado + CatAdj_Quadrado)
print (f'A hipotenusa de um triângulo com catetos {CatOpst} e {CatAdj} é igual a {Hipotenusa} ' )