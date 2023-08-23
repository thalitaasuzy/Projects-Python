N1_1 = None
MediaFinal = None
x = None
N1_2 = None
y = None
N2_1 = None
Media_N1 = None
VALOR = None
N2_2 = None
Media_N2 = None
N1 = None
N2 = None


def text_prompt(msg):
    try:
        return raw_input(msg)
    except NameError:
        return input(msg)


# Aplicar pesos e calcular média
def MediaFinalFunction():
    global N1_1, MediaFinal, x, N1_2, y, N2_1, Media_N1, VALOR, N2_2, Media_N2, N1, N2
    x = Media_N1 * 2
    y = Media_N2 * 3
    VALOR = x + y
    MediaFinal = VALOR / 5
    return MediaFinal


print('##Programa Média Das Etapas##')
N1_1 = float(text_prompt('Informe sua primeira nota na N1: '))
N1_2 = float(text_prompt('Informe sua segunda nota na N1: '))
N2_1 = float(text_prompt('Informe sua primeira nota na N2: '))
N2_2 = float(text_prompt('Informe sua segunda nota na N2: '))
N1 = N1_1 + N1_2
Media_N1 = N1 / 2
print('Média N1')
print(Media_N1)
N2 = N2_1 + N2_2
Media_N2 = N2 / 2
print('Média N2')
print(Media_N2)
print('##Média Final##')
print(MediaFinalFunction())
if MediaFinalFunction() < 3:
    print('REPROVADO!!!:/')
elif MediaFinalFunction() < 6 and MediaFinalFunction() >= 3:
    print('ESTUDAR PARA AVALIAÇÃO FINAL!!!!^^')
elif MediaFinalFunction() >= 6:
    print('APROVADO!!!!!!')
