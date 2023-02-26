'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais  ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
# Ressaltando: O carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('Digite quantos dias você esteve com o carro: '))
km = float(input('Digite quantos km foram rodados: '))
preço = (dia * 60) + (0.15 * km)
print(f'O preço que você precisa pagar é {preço}')