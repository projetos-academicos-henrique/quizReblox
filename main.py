import streamlit as st
import perguntas

perguntas = perguntas.perguntas

if 'game_started' not in st.session_state:
    st.session_state.game_started = False

if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

if 'difficult' not in st.session_state:
    st.session_state.difficult = None

if 'questions' not in st.session_state:
    st.session_state.questions = None

if 'correct_anwsers' not in st.session_state:
    st.session_state.correct_anwsers = 0

if 'lifes' not in st.session_state:
    st.session_state.lifes = 3

def gameOver():
    st.write(f"Vidas: {st.session_state.lifes}")
    st.write(f"Game Over, sua pontuação foi: {st.session_state.correct_anwsers}")

    st.text_input("Seu nome")

def verifyAnswer(userAnswer, correctAnswer):
    if userAnswer == correctAnswer:
        st.write("Resposta correta!")
        st.session_state.correct_anwsers += 1
        return True
    else:
        st.write("Resposta incorreta!")
        st.session_state.lifes -= 1
        return False

def printQuestion(question):
    st.write(question["pergunta"])
    
    current_answer = st.radio("Alternativas:", question["respostas"], key=f"radio_{st.session_state.current_question_index}")
    
    if st.button("Selecionar", key=f"button_{st.session_state.current_question_index}"):
        st.write(f"Você selecionou: {current_answer}")
        verifyAnswer(current_answer, question["respostaCorreta"])

        # Incrementa o índice da pergunta
        st.session_state.current_question_index += 1

        # Verifica se ainda há perguntas
        if st.session_state.current_question_index < len(st.session_state.questions) and st.session_state.lifes > 0:
            quiz()  # Chama a função para exibir a próxima pergunta
        else:
            # st.session_state.game_started = False
            gameOver()

def quiz():
    if st.session_state.difficult == "Fácil":
        st.session_state.questions = perguntas["facil"]
    elif st.session_state.difficult == "Difícil":   
        st.session_state.questions = perguntas["dificil"]
        
    # Exibe a pergunta atual
    printQuestion(st.session_state.questions[st.session_state.current_question_index])

# Lógica para exibir a página selecionada
if st.sidebar.radio("Selecione uma página:", ("Jogar", "LeaderBoard")) == "Jogar":

    if not st.session_state.game_started:
        st.write("""
        # Quiz Reblox
        Bem-vindo ao jogo! Aqui você pode jogar o quiz.
        """)
        difficult = st.radio("Selecione uma dificuldade:", ("Fácil", "Difícil"))
        if st.button("Iniciar Quiz"):
            st.session_state.difficult = difficult  
            st.session_state.game_started = True
            quiz()  
    else:
        st.write(f"Vidas: {st.session_state.lifes}")
        quiz()  
