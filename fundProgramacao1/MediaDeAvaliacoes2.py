#Programinha para calcular notas

def calcMed(a,b):
  return (a + b) / 2
  

print ('Oiê! Esse código é um teste para a programadora aqui atrás treinar. Lets GO 😶‍🌫️')
print ('***** Lembrando que esse metódo é usado para o padrão: duas avaliações na N1 e duas na N2.')

print ('-------------------------- MATEMÁTICA 2 --------------------------')


print ('-------- Começando pela N1... --------')

Av1N1 = float(input('Digite a sua primeira nota da N1: '))
Av2N1 = float(input('Digite a sua segunda nota da N1: '))

MedN1 = calcMed (Av1N1,Av2N1)

if 10 >= MedN1 >= 6:
  print ('Muito beeem pessoa sabida, sua média na N1 é: ', MedN1)
if 0 <= MedN1 < 6:
  print ('Ok, sua situação tá um tiquin complicada, sua média na N1 é: ', MedN1)
else:
  print ('*** Error! Você não escreveu um valor possível ein, pare de quebrar o meu código. ')
  
print ('------- Continuando, aqui vamos nós N2 ---------')

Av1N2 = float(input('Digite a sua pontuação na primeira avaliação da N2: '))
if Av1N1 <= 10 and Av2N1 <= 10 and Av1N2 <= 10:
    QuantoFaltaDeMed = (25 - (MedN1 * 2)) / 3
    precisoTirar = (QuantoFaltaDeMed * 2) - Av1N2
    print("Talvez isso te assuste, MAS NÃO DESANIMA!!! Você ainda precisa tirar um ", precisoTirar, '. Boa Sorte🫠❤️‍🩹')

