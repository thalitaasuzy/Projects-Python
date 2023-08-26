# Calcular (e escrever) a soma dos divisores de determinado número K.

A = 0
B = int(input('Digite um número: '))

def div(B):
    result = [i for i in range(1, B + 1) if B % i == 0]
    return result

Div = (div(B))
print(Div)

A = A + sum(Div)
print(A)
