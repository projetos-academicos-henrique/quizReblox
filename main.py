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
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {"facil":[], "dificil":[]}


st.sidebar.title("Reblox")
opcao = st.sidebar.radio("Escolha uma opção:", ["Quiz", "Leaderboard"])

def resetarJogo():
    st.session_state.dificuldade = None
    st.session_state.perguntaAtual = 0
    st.session_state.pontuacao = 0
    st.session_state.vidas = 3

def salvarPontuação(nome, pontuacao, dificuldade):
    st.session_state.leaderboard[dificuldade].append({'nome': nome, 'pontuacao': pontuacao})
    st.success("Salvo com sucesso")
    resetarJogo()
    time.sleep(1)
    st.rerun()

    

def quiz():

    if st.session_state.vidas > 0:
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
                    time.sleep(1)
                    st.rerun()
    else:
        name = st.text_input("Insira seu nome para salvar sua pontuação")
        if name:
            salvarPontuação(name, st.session_state.pontuacao, st.session_state.dificuldade)

                
                
        
def leaderboard():
    st.title("Leaderboard")
    st.write("Confira as melhores pontuações!")

    st.title("Fácil")

    sorted_facil = sorted(st.session_state.leaderboard["facil"], key=lambda x: x['pontuacao'], reverse=True)

    if(len(sorted_facil) > 0):
        for i, item in enumerate(sorted_facil):
            st.write(f"- {i+1}º - {item['nome']} {item['pontuacao']}")
    else:
        st.write("Não há jogadores nessa categoria ainda")

    st.title("Difícil")

    sorted_dificil = sorted(st.session_state.leaderboard["dificil"], key=lambda x: x['pontuacao'], reverse=True)

    if(len(sorted_dificil) > 0):
        for i, item in enumerate(sorted_dificil):
            st.write(f"- {i+1}º - {item['nome']} {item['pontuacao']}")
    else:
        st.write("Não há jogadores nessa categoria ainda")
        

def main():
    if opcao == "Quiz":
        if st.session_state.dificuldade is None:
            st.title("Quiz")
            st.write("Bem-vindo ao Quiz! Selecione a dificuldade e comece a jogar.")
            if st.button("Fácil"):
                st.session_state.dificuldade = "facil"
                st.rerun()
            if st.button("Difícil"):
                st.session_state.dificuldade = "dificil"
                st.rerun()
        else:
            st.write(f"Vidas: {st.session_state.vidas}")
            st.write(f"Pontuação: {st.session_state.pontuacao}")
            quiz()

    elif opcao == "Leaderboard":
        leaderboard()

main()