vidas = 3
sequencia = 0
acertadas = 0
dificuldade = ""

leaderboardLista = ["sopa", 10, "D", "pedro", 12, "F", "andrey", 12, "D"]
# leaderboardLista = []

perguntasFacil = [
    "Qual é a principal fonte de energia dos carros na Fórmula E?",
    "Gasolina",
    "Diesel",
    "Eletricidade",
    "Etanol",

    "Quantas temporadas de corridas de Fórmula E ocorreram até agora?",
    "4",
    "6",
    "8",
    "10",

    "Em que ano foi realizada a primeira temporada da Fórmula E?",
    "2012",
    "2014",
    "2016",
    "2018",

    "Qual empresa é a fornecedora oficial de pneus para a Fórmula E?",
    "Pirelli",
    "Bridgestone",
    "Michelin",
    "Goodyear",

    "Qual cidade sediou a primeira corrida de Fórmula E?",
    "Londres",
    "Paris",
    "Pequim",
    "Nova York",

    "Quantos carros competem em cada corrida de Fórmula E?",
    "10",
    "12",
    "20",
    "24",

    "Quantas equipes competem atualmente na Fórmula E?",
    "8",
    "10",
    "11",
    "12",

    "Qual é a duração média de uma corrida de Fórmula E?",
    "30 minutos",
    "45 minutos",
    "1 hora",
    "1 hora e 30 minutos",

    "Qual é o nome da temporada 2019-2020 da Fórmula E?",
    "Season 5",
    "Season 6",
    "Season 7",
    "Season 8",

    "Qual é a velocidade máxima aproximada dos carros de Fórmula E?",
    "150 km/h",
    "200 km/h",
    "250 km/h",
    "300 km/h"
]

respostasFacil = ["C", "C", "B", "C", "C", "D", "D", "B", "B", "C"]

perguntasDificil = [
    "Qual equipe venceu a primeira temporada da Fórmula E?",
    "Audi Sport ABT",
    "Renault e.dams",
    "DS Techeetah",
    "Mahindra Racing",

    "Quem foi o primeiro campeão da Fórmula E?",
    "Nelson Piquet Jr.",
    "Sebastien Buemi",
    "Lucas di Grassi",
    "Jean-Eric Vergne",

    "Qual piloto tem mais vitórias na Fórmula E?",
    "Sam Bird",
    "Lucas di Grassi",
    "Sebastien Buemi",
    "Jean-Eric Vergne",

    "Qual é a capacidade da bateria dos carros de Fórmula E Gen3?",
    "45 kWh",
    "52 kWh",
    "54 kWh",
    "60 kWh",

    "Qual é a potência máxima dos carros da Fórmula E durante a corrida?",
    "150 kW",
    "200 kW",
    "250 kW",
    "300 kW",

    "Quantos modos de potência existem na Fórmula E?",
    "2",
    "3",
    "4",
    "5",

    "Qual é a distância máxima que um carro de Fórmula E pode percorrer com uma carga de bateria?",
    "100 km",
    "150 km",
    "200 km",
    "250 km",

    "Quem é o fundador e CEO da Fórmula E?",
    "Alejandro Agag",
    "Jean Todt",
    "Bernie Ecclestone",
    "Chase Carey",

    "Em qual cidade está localizada a sede da Fórmula E?",
    "Londres",
    "Paris",
    "Nova York",
    "Berlim",

    "Qual é o nome do sistema que permite aos fãs votarem para dar um impulso de potência aos seus pilotos favoritos?",
    "FanBoost",
    "PowerVote",
    "EnergyBoost",
    "SpeedVote"
]

respostasDificil = ["B", "A", "C", "C", "C", "B", "B", "A", "A", "A"]

respostas = []
perguntas = []

def mostrarVidasSequencia():
    print(f"Vidas: {vidas}")
    print(f"Sequencia de acertos: {sequencia}")

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

def addLeaderboard():
    leaderboardLista.append(input("Digite seu nome para adicionar à leaderboard: "))
    leaderboardLista.append(acertadas)
    leaderboardLista.append(dificuldade)

def gameOver():
    if vidas <= 0:
        mostrarVidasSequencia()
        print("Game Over! Você ficou sem vidas!")
        addLeaderboard()
        print("Voltando ao menu... \n")
        menu()

def addVida():
    if sequencia % 5 == 0:
        vidas += 1
        print("5 acertos seguidos! Ganhou uma vida!")

def validarResposta(alternativa):
    alternativa = alternativa.upper()
    return alternativa == "A" or alternativa == "B" or alternativa == "C" or alternativa == "D"

def quiz():
    global dificuldade, respostas, perguntas

    print("Escolha a dificuldade:")
    print("F - Fácil")
    print("D - Difícil")

    dificuldade = input("Sua escolha: ").upper()
   
    while True:
        if dificuldade == "F":
            respostas = respostasFacil
            perguntas = perguntasFacil
            print("Dificuldade Fácil escolhida")
            break
        elif dificuldade == "D":
            respostas = respostasDificil
            perguntas = perguntasDificil
            print("Dificuldade Difícil escolhida")
            break
        else:
            print("Insira uma dificuldade válida!")
            dificuldade = input("Sua escolha: ")

    for i in range(0, len(perguntas), 5):
        print(perguntas[i])
        print(f"A) {perguntas[i + 1]}")
        print(f"B) {perguntas[i + 2]}")
        print(f"C) {perguntas[i + 3]}")
        print(f"D) {perguntas[i + 4]}")

        resposta = input("Sua resposta: ")

        while not validarResposta(resposta):
            print("Alternativa inválida")
            resposta = input("Sua resposta: ")

        conferirResposta(int(i/5), resposta, respostas)

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

    print("Fácil")
    print("------")
    for i in range(0, len(lista_F)):
        item = lista_F[i]
        print(f"{i + 1} - {item[1]} - {item[0]} acertos")

    print("\n")
    print("Difícil")
    print("------")

    for i in range(0, len(lista_D)):
        item = lista_D[i]
        print(f"{i + 1} - {item[1]} - {item[0]} acertos")
    print("\n")

    input("Digite qualquer coisa para voltar para o menu... \n")
    menu()

def menu():
    global sequencia, vidas, acertadas, dificuldade

    vidas = 3
    sequencia = 0
    acertadas = 0
    dificuldade = ""

    print("Bem vindo ao quiz Reblox!!!")
    print("1 - Jogar")
    print("2 - Leaderboard")
    print("0 - Sair")

    opcao = int(input("Sua opção: "))

    if opcao == 1:
        quiz()
    elif opcao == 2:
        leaderboard()
    elif opcao == 0:
        return

menu()
