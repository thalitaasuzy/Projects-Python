# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print ('Digite os dados da parede ')
l = float(input('Largura: '))
h = float(input('Altura: '))

print (f'A área da parede é de aproximadamente {l*h:.3f} metros², considerando que você use 2l por m², você precisa de {l*h/2:.3f} l de tinta.')