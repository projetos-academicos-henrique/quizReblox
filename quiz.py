vidas = 3
sequencia = 0
acertadas = 0
dificuldade = ""

leaderboardLista = ["sopa", 10, "D", "pedro", 12, "F", "andrey", 12, "D"]

perguntasFacil = ["Qual é a principal fonte de energia dos carros na Formula E?",
  "Gasolina",
  "Diesel",
  "Eletricidade",
  "Etanol",

  "Quantas temporadas de corridas de Formula E ocorreram até agora?",
  "4",
  "6",
  "8",
  "10"

]

perguntasDificil = []

respostasDificil = []

respostasFacil = ["C","B"]


respostas = []
perguntas = []


def mostrarVidasSequencia():

  print(f"Vidas: {vidas}")
  print(f"Sequencia de acertos: {sequencia}")


def conferirResposta(index,alternativa, listaRespostas):

  global sequencia, vidas,acertadas

  alternativa = alternativa.upper()

  if alternativa == listaRespostas[index]:
     sequencia += 1
     acertadas += 1
     addVida()
     print("Parabens! Voce acertou!")

  else:
     vidas -= 1
     sequencia = 0
     gameOver()

     print("Ixe! Parece que voce errou...")

  mostrarVidasSequencia()

def addLeaderboard():
   leaderboardLista.append(input("Digite seu nome para adicionar a leaderboard: "))
   leaderboardLista.append(acertadas)
   leaderboardLista.append(dificuldade)

def gameOver():
   if vidas <= 0:
    mostrarVidasSequencia()
    print("Game Over! Voce ficou sem vidas!")
    addLeaderboard()
    print("Voltando ao menu... \n")
    menu()

def addVida():
   if sequencia % 5 == 0:
      vidas += 1
      print("5 acertos sequidos! Ganhou uma vida!")


def validadarResposta(alternativa):

  alternativa = alternativa.upper()

  return alternativa == "A" or alternativa == "B" or alternativa == "C" or alternativa == "D"


def quiz():

    global dificuldade

    print("Escolha a dificuldade:")
    print("F - Fácil")
    print("D - Difícil")

    dificuldade = input("Sua escolha: ").upper()
   
    while True:
        if dificuldade == "F":
            respostas = respostasFacil
            perguntas = perguntasFacil
            print("Dificuldade Facil escolhidas")
            break
        elif dificuldade == "D":
            respostas = respostasDificil
            perguntas = perguntasDificil
            print("Dificuldade Dificil escolhidas")
            break
        else:
            print("Insira uma dificuldade valida!")
            dificuldade = input("Sua escolha: ")


    for i in range(0, len(perguntas), 5):

        print(perguntas[i])

        print(f"A) {perguntas[i + 1]}")
        print(f"B) {perguntas[i + 2]}")
        print(f"C) {perguntas[i + 3]}")
        print(f"D) {perguntas[i + 4]}")


        resposta = input("Sua resposta: ")

        while not validadarResposta(resposta):
            print("Alternativa invalida")
            resposta = input("Sua resposta: ")

        conferirResposta(int(i/5),resposta, respostas)

    print("Fim de jogo!")
    addLeaderboard()
    menu()


def leaderboard():



    lista_D = []
    lista_F = []

    for i in range(0, len(leaderboardLista), 3):
        nome = leaderboardLista[i]
        pontuacao = leaderboardLista[i + 1]
        tipo = leaderboardLista[i + 2]
        if tipo == "D":
            lista_D.append((pontuacao, nome))
        elif tipo == "F":
            lista_F.append((pontuacao, nome))

    lista_D.sort(reverse=True)
    lista_F.sort(reverse=True)

    print("Facil")
    print("------")
    for i in range(0, len(lista_F)):
        item = lista_F[i]
        print(f"{i + 1} - {item[1]} - {item[0]} acertos")

    print("\n")
    print("Dificil")
    print("------")

    for i in range(0, len(lista_D)):
        item = lista_D[i]
        print(f"{i + 1} - {item[1]} - {item[0]} acertos")
    print("\n")


    input("Digite qualquer coisa para voltar para o menu... \n")
    menu()

    


def menu():
   global sequencia, vidas,acertadas,dificuldade

   vidas = 3
   sequencia = 0
   acertadas = 0
   dificuldade = ""

   print("Bem vindo ao quiz Reblox!!!")

   print("1 - Jogar")
   print("2 - Leaderboard")
   print("0 - Sair")

   opcao = int(input("Sua opcao: "))

   if opcao == 1:
    quiz()
   elif opcao == 2:
    leaderboard()
   elif opcao == 0:
    return
      

   
menu()
