#Escreva um programa que leia um valor em metros e o exiba convertido em outras medidas.

m = float(input('Distância em metros: '))

print(f'A distância de {m} metros corresponde a: ')
print(f'{(m / 1000)} km')
print(f'{(m/100)} hm')
print(f'{(m/10)} dam')
print(f'{(m*10)} dm')
print(f'{m*100} cm')
print(f'{(m*1000)} mm')
