# Calcular (e escrever) a soma dos divisores de determinado número K.

A = 0
B = int(input('Digite um número: '))

def div(B):
    resultado = [i for i in range(1, B + 1) if B % i == 0]
    
    return resultado


Div = (div(B))
print(Div)

for d in Div:
   while A < sum(Div):
    A = A + d
  
print(A)

for x in Div:
  print(x, Div.count(x), 0)
