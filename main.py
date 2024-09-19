import streamlit as st
import perguntas
import time

perguntas = perguntas.perguntas

if 'dificuldade' not in st.session_state:
    st.session_state.dificuldade = None
if 'perguntaAtual' not in st.session_state:
    st.session_state.perguntaAtual = 0
if 'pontuacao' not in st.session_state:
    st.session_state.pontuacao = 0
if 'vidas' not in st.session_state:
    st.session_state.vidas = 3

st.sidebar.title("Reblox")
opcao = st.sidebar.radio("Escolha uma opção:", ["Quiz", "Leaderboard"])

def resetarJogo():
    st.session_state.dificuldade = None
    st.session_state.perguntaAtual = 0
    st.session_state.pontuacao = 0
    st.session_state.vidas = 3

def quiz():
    st.write(perguntas[st.session_state.dificuldade][st.session_state.perguntaAtual]["pergunta"])
    for item in perguntas[st.session_state.dificuldade][st.session_state.perguntaAtual]["respostas"]:
        if st.button(item):
            if item == perguntas[st.session_state.dificuldade][st.session_state.perguntaAtual]["respostaCorreta"]:
                st.success("Resposta correta!")
                st.session_state.pontuacao += 1
            else:
                st.error("Resposta incorreta!")
                st.session_state.vidas -= 1
            if st.session_state.vidas > 0:
                st.session_state.perguntaAtual += 1
                time.sleep(1)
                st.rerun()
            else:
                st.error("Fim de jogo! Você perdeu todas as vidas.")
                
                
        
def leaderboard():
    st.title("Leaderboard")
    st.write("Confira as melhores pontuações!")

def main():
    if opcao == "Quiz":
        st.title("Quiz")
        st.write("Bem-vindo ao Quiz! Selecione a dificuldade e comece a jogar.")
        st.write(f"Vidas: {st.session_state.vidas}")
        st.write(f"Pontuação: {st.session_state.pontuacao}")
        if st.session_state.dificuldade is None:
            if st.button("Fácil"):
                st.session_state.dificuldade = "facil"
                st.rerun()
            if st.button("Difícil"):
                st.session_state.dificuldade = "dificil"
                st.rerun()
        else:
            quiz()

    elif opcao == "Leaderboard":
        leaderboard()

main()