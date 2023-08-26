'''
PROBLEMAS PARA SEREM RESOLVIDOS COM ESTRUTURA “FOR” -
PART 1
'''

#1 - a) Escrever os números de 1 (um) até 50 (cinquenta).

for X in range (1,51) : 
  print (X)

#2 - b) Escrever os números de 1 (um) até determinado número N lido por um “input”.
N = int(input("Em qual número devemos parar? "))
for X in range (1, N + 1):
        print (X)

#3 - c) Escrever os números entre A e B, ambos lidos por comandos “input”.
A = int(input('Digite o valor inicial A: '))
B = int(input('Digite o valor final B: '))
for X in range (A, B + 1):
  print(X)

#4 - d) Escrever os múltiplos de 3 (três) em um intervalo [A , B].
A = int(input('Digite o valor A inicial do intervalo: '))
B = int(input('Digite o valor B final do intervalo: '))
for X in range (A, B + 1):
   if (X % 3 == 0):
     print(X)

#5 - e) Escrever os múltiplos de 5 (cinco) em um intervalo [A , B].
A = int(input('Digite valor inicial A para o intervalo: '))
B = int(input('Digite o valor final B para o intervalo: '))
for X in range (A, B + 1):
  if (X % 5 == 0):
    print(X)

### NICE, WE GET IT!!!!! 🥳 🥳 🥳 🥳 🥳###

     
