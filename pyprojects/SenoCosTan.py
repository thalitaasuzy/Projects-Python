#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
Angulo = float(input('Digite o valor do Ângulo: '))
ConvertRad = math.radians(Angulo)
sen = math.sin(ConvertRad)
cos = math.cos(ConvertRad)
tan = math.tan(ConvertRad)
print (f'O seno do ângulo {Angulo} é {sen:.2f};')
print (f'O cosseno do ângulo {Angulo} é {cos:.2f};')
print (f'A tangente do ângulo {Angulo} é {tan:.2f};')
print (f'Bônus: O valor de {Angulo} graus em radianos é {ConvertRad} rad. ')

