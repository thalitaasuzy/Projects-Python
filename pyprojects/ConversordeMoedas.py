#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Quantos reais você têm: '))
d = 5.29
e = 5.67

print(f'Com R${r:.2f} você pode comprar US${r/d:.2f} [dolláres] e Є{r/e:.2f} [euros]')