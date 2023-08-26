Name = input("Olá. Qual seu nome? ")
print()

Welcome_Txt = "Prazer, {}. Eu sou a sua nova maneira de passar o tédio =)" .format (Name)

print (Welcome_Txt)

print ("Você tem um nome muito bonito, {}. Que tal escolher um para mim?" .format(Name))
print()
AssistentName = input("Digite um nome: ")

print ()
print ("-------------------PROCESSANDO-------------------")
print ()

print ("Certo, eu até que gostei!! A partir de agora só me chame de {}, boot{} ou {}zinh@, para os mais próximos. " .format(AssistentName, AssistentName, AssistentName))
 
print ()

Resposta = input("Quer ver uma coisa legal? ")
print()
print("{}??? Eu não estava esperando por isso... Brincadeira!!! Eu estava esperando sim😁. É que na verdade sua resposta não importa. Eu ainda não sei fazer muita coisa, sabe? Tenho que demonstrar minhas poucas habilidades. Como essa:" .format(Resposta))

print()

Language = float(input("Escolha um número de {} à {}, por favor. )  ------- " .format (1,4)))

print()
print("Alô, banco de dados? O que é que o número {} faz mes...?" .format(Language))
print()

txt1 = "My name is {Fname}, I'm a few minutes of 'life'. " .format(Fname = AssistentName)

txt2 = "Je m'appelle {0}, j'ai quelques minutes à vivre. " .format(AssistentName)

txt3 = "Mi nombre es {}, tengo pocos minutos de vida." .format(AssistentName)

txt4 = "Mi chiamo {}, ho pochi minuti da vivere." .format(AssistentName)

if Language == 1:
  print (txt1)
  print()
  print ("Do you liked? É assim que eu me apresento em inglês.") 
if Language == 2:
  print (txt2)
  print()
  print ("As-tu aimé?? É assim que eu me apresento em francês.")
if Language == 3:
  print (txt3)
  print()
  print ("¿Te gustó? É assim que eu me apresento em espanhol.")
if Language == 4:
  print (txt4)
  print()
  print ("Ti è piaciuto?? É assim que eu me apresento em italiano.")
if 0 < Language < 5:
  print ("A tradução é: 'Meu nome é {}. Tenho alguns minutos de vida'." .format (AssistentName))
if Language != 1 and Language != 2 and Language != 3 and Language != 4:
  print ("ERROR! Ei, {} eu te dei opções!!! Calma ai que eu não sou nenhuma inteligência artificial para saber responder a qualquer coisa que você quiser colocar. Isso é coisa da Google, Siri, Alexa... Eu ainda sou um/uma bebê. " .format (Name))

Age = int(input("De qualquer forma, foi muito legal te conhecer {} não bilíngue. Quantos anos você tem mesmo?  " .format(Name)))

print()

Days = Age * 365 
Ano = 2022 - Age 


print (Name, "de {} anos, nasceu em {} isso dá aproximadamente {} dias de vida (Desconsiderando os anos bissextos e seu aniversário, porque aqui só quem sabe matemática é o desktop mesmo.) " .format(Age, Ano,  Days))


print()
print('Cê tá ficando véi, ein. Cuidado com as juntas! Agora eu preciso ir, acho que deu um problema e tem uma coisa aqui no barramen... TCHAUUUU! NÃO ESQUECE DE TESTAR OS OUTROS NÚMEROS EIN. BJO NA ORELHA <3')
print()
print("----------------------------------------------------------------------------------------------------")
print("Brincadeiras à parte. Obrigada por testar o código, {} :). Foi uma brincadeira para testar o comando .format() e descobrir qual a sua finalidade, ao ponto que eu acabei me empolgando. Boa sorte com qualquer coisa que você esteja fazendo. Hidrate-se, seu rins agradecem!!! ByeBye" .format (Name))
print()
print()
print()
print("./ass: Thalita")