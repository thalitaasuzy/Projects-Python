#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# 5% de desconto = Valor Total - 0.5% (5/100) * Valor Total
p = float(input('Preço do produto que deseja comprar: '))
d = p * 0.05
pd = p - d
print(f'O valor do produto com desconto de 5% é RS{pd}')

