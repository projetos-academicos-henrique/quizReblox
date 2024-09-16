import perguntas

perguntas = perguntas.perguntas

#Declara variaveis globais
vidas = 3
sequencia = 0
acertadas = 0
dificuldade = ""

leaderboardLista = {
    "facil": [
    ],
    "dificil": [

    ]
}

respostas = []

#funcao para exibir as vidas e a sequnecia do usuario

def mostrarVidasSequencia():
    print(f"Vidas: {vidas}")
    print(f"Sequencia de acertos: {sequencia}")

#funcao que confere se a resposta da foi correta

def conferirResposta(index, alternativa, listaRespostas):
    global sequencia, vidas, acertadas

    alternativa = alternativa.upper()

    if alternativa == listaRespostas[index]:
        sequencia += 1
        acertadas += 1
        addVida()
        print("Parabéns! Você acertou!")
    else:
        vidas -= 1
        sequencia = 0
        print("Ixe! Parece que você errou...")
        gameOver()

    mostrarVidasSequencia()

#adiciona o usuario atual a leaderboard

def addLeaderboard():
    
    nome = input("Digite seu nome para adicionar à leaderboard: ")
    user = {
        "nome": nome,
        "pontuacao": acertadas
    }
    
    if dificuldade == "F":
        leaderboardLista["facil"].append(user)
    elif dificuldade == "D":
        leaderboardLista["dificil"].append(user)

#finaliza um jogo

def gameOver():
    if vidas <= 0:
        mostrarVidasSequencia()
        print("Game Over! Você ficou sem vidas!")
        addLeaderboard()
        print("Voltando ao menu... \n")
        menu()

#Adiciona uma vida ao ususario se a sequencia dele for divisivel por 5

def addVida():
    global vidas
    if sequencia % 5 == 0:
        vidas += 1
        print("5 acertos seguidos! Ganhou uma vida!")

#valida as respostas possiveis do usuario

def validarResposta(alternativa):
    alternativa = alternativa.upper()
    return alternativa == "A" or alternativa == "B" or alternativa == "C" or alternativa == "D"

#comeca a exebir perguntas e pedir respostas

def quiz():
    global dificuldade, respostas, perguntas

    print("Escolha a dificuldade:")
    print("F - Fácil")
    print("D - Difícil")

    dificuldade = input("Sua escolha: ").upper()
    print("")


    while True:
        if dificuldade == "F":
            respostas = [pergunta["respostaCorreta"] for pergunta in perguntas["facil"]]
            perguntas = perguntas["facil"]
            print("Dificuldade Fácil escolhida")
            print("")
            break
        elif dificuldade == "D":
            respostas = [pergunta["respostaCorreta"] for pergunta in perguntas["dificil"]]
            perguntas = perguntas["dificil"]
            print("Dificuldade Difícil escolhida")
            print("")
            break
        else:
            print("Insira uma dificuldade válida!")
            dificuldade = input("Sua escolha: ").upper()

    for i, pergunta in enumerate(perguntas):
        print(pergunta["pergunta"])
        for j, resposta in enumerate(pergunta["respostas"]):
            print(f"{chr(65 + j)} - {resposta}")

        resposta = input("Sua resposta: ")

        while not validarResposta(resposta):
            print("Alternativa inválida")
            resposta = input("Sua resposta: ")

        conferirResposta(i, resposta, respostas)

    print("Fim de jogo!")
    addLeaderboard()
    menu()

# ordena, separa e exibe a lista de pontuacoes

def leaderboard():

    for dificuldade in leaderboardLista:
        print(f"{dificuldade}")
        print("------")
        
        listaOrdenada = sorted(leaderboardLista[dificuldade], key=lambda x: x['pontuacao'], reverse=True)
        
        for i in range(0, len(listaOrdenada)):
            print(f"{i + 1}º - {listaOrdenada[i]['nome']} - {listaOrdenada[i]['pontuacao']} acertos")
        
        print("\n")

    input("Digite qualquer coisa para voltar para o menu... \n")
    print("")
    menu()

#exibe menu principal

def menu():
    global sequencia, vidas, acertadas, dificuldade

    vidas = 3
    sequencia = 0
    acertadas = 0
    dificuldade = ""

    while True:

        print("Bem vindo ao quiz Reblox!!!")
        print("1 - Jogar")
        print("2 - Leaderboard")
        print("0 - Sair")

        opcao = input("Sua opção: ")
        print("")

        if opcao == "1":
            quiz()
        elif opcao == "2":
            leaderboard()
        elif opcao == "0":
            print("Até a proxima!")
            break
        else:
            print("Digite uma opção válida\n")

menu()
