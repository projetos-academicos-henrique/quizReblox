from pyscript import document
from js import localStorage

perguntas = {
    "facil": [
        {
            "pergunta": "Qual é a principal fonte de energia dos carros na Fórmula E?",
            "respostas": [
                "Gasolina",
                "Diesel",
                "Eletricidade",
                "Etanol"
            ],
            "respostaCorreta": "C"
        },
        {
            "pergunta": "Quantas temporadas de corridas de Fórmula E ocorreram até agora?",
            "respostas": [
                "4",
                "6",
                "8",
                "10"
            ],
            "respostaCorreta": "C"
        },
        {
            "pergunta": "Em que ano foi realizada a primeira temporada da Fórmula E?",
            "respostas": [
                "2012",
                "2014",
                "2016",
                "2018"
            ],
            "respostaCorreta": "B"
        },
        {
            "pergunta": "Qual empresa é a fornecedora oficial de pneus para a Fórmula E?",
            "respostas": [
                "Pirelli",
                "Bridgestone",
                "Michelin",
                "Goodyear"
            ],
            "respostaCorreta": "C"
        },
        {
            "pergunta": "Qual cidade sediou a primeira corrida de Fórmula E?",
            "respostas": [
                "Londres",
                "Paris",
                "Pequim",
                "Nova York"
            ],
            "respostaCorreta": "C"
        },
        {
            "pergunta": "Quantos carros competem em cada corrida de Fórmula E?",
            "respostas": [
                "10",
                "12",
                "20",
                "24"
            ],
            "respostaCorreta": "D"
        },
        {
            "pergunta": "Quantas equipes competem atualmente na Fórmula E?",
            "respostas": [
                "8",
                "10",
                "11",
                "12"
            ],
            "respostaCorreta": "D"
        },
        {
            "pergunta": "Qual é a duração média de uma corrida de Fórmula E?",
            "respostas": [
                "30 minutos",
                "45 minutos",
                "1 hora",
                "1 hora e 30 minutos"
            ],
            "respostaCorreta": "B"
        },
        {
            "pergunta": "Qual é o nome da temporada 2019-2020 da Fórmula E?",
            "respostas": [
                "Season 5",
                "Season 6",
                "Season 7",
                "Season 8"
            ],
            "respostaCorreta": "B"
        },
        {
            "pergunta": "Qual é a velocidade máxima aproximada dos carros de Fórmula E?",
            "respostas": [
                "150 km/h",
                "200 km/h",
                "250 km/h",
                "300 km/h"
            ],
            "respostaCorreta": "C"
        }
    ],
    "dificil": [
        {
            "pergunta": "Qual equipe venceu a primeira temporada da Fórmula E?",
            "respostas": [
                "Audi Sport ABT",
                "Renault e.dams",
                "DS Techeetah",
                "Mahindra Racing"
            ],
            "respostaCorreta": "B"
        },
        {
            "pergunta": "Quem foi o primeiro campeão da Fórmula E?",
            "respostas": [
                "Nelson Piquet Jr.",
                "Sebastien Buemi",
                "Lucas di Grassi",
                "Jean-Eric Vergne"
            ],
            "respostaCorreta": "A"
        },
        {
            "pergunta": "Qual piloto tem mais vitórias na Fórmula E?",
            "respostas": [
                "Sam Bird",
                "Lucas di Grassi",
                "Sebastien Buemi",
                "Jean-Eric Vergne"
            ],
            "respostaCorreta": "C"
        },
        {
            "pergunta": "Qual é a capacidade da bateria dos carros de Fórmula E Gen3?",
            "respostas": [
                "45 kWh",
                "52 kWh",
                "54 kWh",
                "60 kWh"
            ],
            "respostaCorreta": "C"
        },
        {
            "pergunta": "Qual é a potência máxima dos carros da Fórmula E durante a corrida?",
            "respostas": [
                "150 kW",
                "200 kW",
                "250 kW",
                "300 kW"
            ],
            "respostaCorreta": "C"
        },
        {
            "pergunta": "Quantos modos de potência existem na Fórmula E?",
            "respostas": [
                "2",
                "3",
                "4",
                "5"
            ],
            "respostaCorreta": "B"
        },
        {
            "pergunta": "Qual é a distância máxima que um carro de Fórmula E pode percorrer com uma carga de bateria?",
            "respostas": [
                "100 km",
                "150 km",
                "200 km",
                "250 km"
            ],
            "respostaCorreta": "B"
        },
        {
            "pergunta": "Quem é o fundador e CEO da Fórmula E?",
            "respostas": [
                "Alejandro Agag",
                "Jean Todt",
                "Bernie Ecclestone",
                "Chase Carey"
            ],
            "respostaCorreta": "A"
        },
        {
            "pergunta": "Em qual cidade está localizada a sede da Fórmula E?",
            "respostas": [
                "Londres",
                "Paris",
                "Nova York",
                "Berlim"
            ],
            "respostaCorreta": "A"
        },
        {
            "pergunta": "Qual é o nome do sistema que permite aos fãs votarem para dar um impulso de potência aos seus pilotos favoritos?",
            "respostas": [
                "FanBoost",
                "PowerVote",
                "EnergyBoost",
                "SpeedVote"
            ],
            "respostaCorreta": "A"
        }
    ]
}

quizEl = document.querySelector("#quiz")
currentQuestionIndex = 0
perguntasSelecionadas = []

correctAnwsers = 0
lifes = 3
sequence = 0
namePlayer = ""

import json

leaderboard = {
    "facil": [],
    "dificil": []
}

def clearQuiz():
    quizEl.innerHTML = ""

def saveData():
    global namePlayer, correctAnwsers, leaderboard
    
    if namePlayer:
        difficulty = "facil" if perguntasSelecionadas == perguntas["facil"] else "dificil"
        leaderboard[difficulty].append({"nome": namePlayer, "pontuacao": correctAnwsers})
        
        # Ordenar o leaderboard
        leaderboard[difficulty] = sorted(leaderboard[difficulty], key=lambda x: x['pontuacao'], reverse=True)
        
        # Salvar no armazenamento local
        localStorage.setItem("leaderboard", json.dumps(leaderboard))

def loadData():
    global leaderboard
    stored_leaderboard = localStorage.getItem("leaderboard")
    if stored_leaderboard:
        leaderboard = json.loads(stored_leaderboard)

def addLife():
    global lifes, sequence
    if sequence > 0 and sequence % 5 == 0:
        lifes += 1
        print("5 acertos seguidos! Ganhou uma vida!")

def showMenu(event = False):

    saveData()

    clearQuiz()


    buttonJogar = document.createElement("button")
    buttonJogar.innerText = "Jogar"
    buttonJogar.setAttribute("py-click", "selectDifficult")
    
    buttonLeaderboard = document.createElement("button")
    buttonLeaderboard.innerText = "Placar"
    buttonLeaderboard.setAttribute("py-click", "showLeaderboard")
    
    quizEl.appendChild(buttonJogar)
    quizEl.appendChild(buttonLeaderboard)

def selectDifficult(event):

    clearQuiz()

    dificultDiv = document.createElement("div")
    dificultDiv.classList.add("menu")

    buttonFacil = document.createElement("button")
    buttonFacil.innerText = "Fácil"
    buttonFacil.value = "F"
    buttonFacil.setAttribute("py-click", "quiz")

    buttonDificil = document.createElement("button")
    buttonDificil.innerText = "Difícil"
    buttonDificil.value = "D"
    buttonDificil.setAttribute("py-click","quiz")

    dificultDiv.appendChild(buttonFacil)
    dificultDiv.appendChild(buttonDificil)

    quizEl.appendChild(dificultDiv)

def quiz(event):

    global perguntasSelecionadas, currentQuestionIndex

    currentQuestionIndex = 0

    clearQuiz()

    difficult = event.target.value

    while True:
        if difficult == "F":
            perguntasSelecionadas = perguntas["facil"]
            break
        elif difficult == "D":
            perguntasSelecionadas = perguntas["dificil"]
            break
        else:
            print("Dificuldade inválida!")

    question()

def showStatus():

    clearQuiz()

    statusEl = document.createElement("div")
    statusEl.classList.add("status")

    statusEl.innerHTML = f"""
    <p>Vidas: {lifes}</p>
    <p>Sequência: {sequence}</p>
    <p>Acertos: {correctAnwsers}</p>
    """

    quizEl.appendChild(statusEl)
    

def question():

    global perguntasSelecionadas

    clearQuiz()

    showStatus()

    currentQuestion = perguntasSelecionadas[currentQuestionIndex]

    question = currentQuestion["pergunta"]
    answers = currentQuestion["respostas"]

    questionDiv = document.createElement("div")
    questionDiv.classList.add("question")

    questionEl = document.createElement("p")
    questionEl.innerHTML = question

    answersEl = document.createElement("div")
    answersEl.classList.add("answers")

    for i, answer in enumerate(answers):
        answerEl = document.createElement("button")
        answerEl.setAttribute("py-click","verifyAnswer")
        answerEl.innerText = answer
        answerEl.value = chr(65 + i)

        answersEl.appendChild(answerEl)

    questionDiv.appendChild(questionEl)
    questionDiv.appendChild(answersEl)

    quizEl.appendChild(questionDiv)

def verifyAnswer(event):

    global perguntasSelecionadas, currentQuestionIndex, correctAnwsers, lifes, sequence

    currentAnswer = perguntasSelecionadas[currentQuestionIndex]["respostaCorreta"]
    selectedAnswer = event.target.value

    if currentAnswer == selectedAnswer:
        print("acertou")
        correctAnwsers += 1
        sequence += 1
        addLife()
    else:
        print("errou")
        sequence = 0
        lifes -= 1

    if lifes <= 0 or currentQuestionIndex >= len(perguntasSelecionadas) - 1:
        gameOver()
    else:
        currentQuestionIndex += 1
        question()

def gameOver():

    global namePlayer

    clearQuiz()

    correctAnwsersEl = document.createElement("p")
    correctAnwsersEl.innerHTML = "Respostas corretas: " + str(correctAnwsers)

    inputName = document.createElement("input")
    inputName.setAttribute("id", "playerName")
    inputName.setAttribute("placeholder", "Insira seu nome")

    buttonSave = document.createElement("button")
    buttonSave.innerText = "Salvar"
    buttonSave.setAttribute("py-click", "saveScore")
    
    quizEl.appendChild(correctAnwsersEl)
    quizEl.appendChild(inputName)
    quizEl.appendChild'(buttonSave)

def saveScore(event):
    global namePlayer
    namePlayer = document.querySelector("#playerName").value
    showMenu()

def showLeaderboard(event):
    clearQuiz()
    
    leaderboardEl = document.createElement("div")
    leaderboardEl.classList.add("leaderboard")
    
    for difficulty in leaderboard:
        difficultyEl = document.createElement("div")
        difficultyEl.innerHTML = f"<h2>{difficulty.capitalize()}</h2>"
        
        for i, player in enumerate(leaderboard[difficulty][:10]):
            playerEl = document.createElement("p")
            playerEl.innerHTML = f"{i+1}. {player['nome']} - {player['pontuacao']} pontos"
            difficultyEl.appendChild(playerEl)
        
        leaderboardEl.appendChild(difficultyEl)
    
    buttonMenu = document.createElement("button")
    buttonMenu.innerText = "Menu"
    buttonMenu.setAttribute("py-click", "showMenu")
    
    quizEl.appendChild(leaderboardEl)
    quizEl.appendChild(buttonMenu)

def startGame():
    loadData()
    showMenu()  

startGame()
