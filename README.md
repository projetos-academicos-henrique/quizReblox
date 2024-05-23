# Quiz Reblox - Fórmula E

## Integrantes

- **Nome**: Andrey
- **RM**: 555339
- **Nome**: Henrique
- **RM**: 554493
- **Nome**: Oliver
- **RM**: 554954
- **Nome**: Pedro Gutierre
- **RM**: 555445
- **Nome**: William
- **RM**: 555132

## Descrição do Projeto

Este projeto consiste em um quiz interativo sobre a Fórmula E, desenvolvido em Python. O quiz tem como objetivo educar e entreter os usuários, aumentando o conhecimento sobre a Fórmula E de maneira gamificada. 

Os jogadores podem escolher entre dois níveis de dificuldade: fácil e difícil. Eles terão um número limitado de vidas e precisarão responder corretamente às perguntas para avançar no jogo. O projeto também inclui uma leaderboard que classifica os jogadores com base na pontuação e dificuldade escolhida.

Além disso, você pode aprender tudo o que precisa sobre a Fórmula E na experiência do Reblox no Roblox, onde um ambiente virtual imersivo recria o evento de uma corrida, incluindo a entrada, as lojas e, claro, a pista.

## Instruções de Uso

1. **Clonar o Repositório**
   ```sh
   git clone https://github.com/seu-usuario/quiz-roblox-formula-e.git
   cd quiz-roblox-formula-e
   ```

2. **Executar o Quiz**
   Certifique-se de ter o Python instalado em sua máquina. Para iniciar o quiz, execute o seguinte comando:
   ```sh
   python quiz.py
   ```

3. **Navegação no Menu**
   - **Jogar:** Selecione a opção "1" para iniciar o quiz.
   - **Leaderboard:** Selecione a opção "2" para visualizar a leaderboard.
   - **Sair:** Selecione a opção "0" para sair do jogo.

4. **Responder às Perguntas**
   - Após iniciar o jogo, escolha a dificuldade (Fácil ou Difícil).
   - Responda às perguntas digitando a letra correspondente à alternativa correta (A, B, C, D).
   - A cada 5 respostas corretas consecutivas, o jogador ganha uma vida extra.

5. **Leaderboard**
   - No final do jogo ou quando o jogador ficar sem vidas ou terminar todas perguntas, será solicitado a inserir seu nome para adicionar à leaderboard.
   - A leaderboard mostra as pontuações dos jogadores, separadas por dificuldade.

## Estrutura do Código

- **quiz.py:** Arquivo principal contendo a lógica do jogo e a interação com o usuário.

## Funcionalidades

- **Mostrar Vidas e Sequência de Acertos:** Mostra o número atual de vidas e a sequência de respostas corretas.
- **Conferir Resposta:** Verifica se a resposta do jogador está correta e atualiza as vidas e sequência de acertos.
- **Adicionar à Leaderboard:** Adiciona a pontuação do jogador à leaderboard no final do jogo.
- **Validação de Respostas:** Garante que o jogador insira uma resposta válida (A, B, C ou D).
- **Quiz:** Função principal que gerencia a seleção de dificuldade, exibição de perguntas e coleta de respostas.
- **Leaderboard:** Exibe a leaderboard com as pontuações dos jogadores.
- **Menu:** Interface inicial do jogo que permite ao jogador escolher entre jogar, ver a leaderboard ou sair.
