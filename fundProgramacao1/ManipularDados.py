Nunca = 1
Raramente = 2
AlgumasVezes = 3
Constantemente = 4
Sempre = 5

Dados = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5 ]

'''Printar dados'''

Dados.sort()
print(Dados)

'''Média'''

M = sum(Dados) / len(Dados)
print (M)

'''Frequência'''
for x in range(0, 6):
  print(x, Dados.count(x), 0)

'''Porcentagem'''

P = (Dados.count(x) / len(Dados) * 100)
print (P)
