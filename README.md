# Slot Machine Game 🎰

Este é um **simulador de máquina caça-níqueis (slot machine)** desenvolvido em Python. O jogo permite que os jogadores façam apostas, girem os rolos e ganhem prêmios com base nos símbolos alinhados. É um projeto simples, mas divertido, que demonstra conceitos básicos de programação, como manipulação de listas, dicionários, loops e funções.

## Funcionalidades ✨

- **Depósito Inicial:** O jogador começa depositando uma quantia de dinheiro.
- **Escolha de Linhas:** O jogador pode escolher em quantas linhas deseja apostar (de 1 a 3).
- **Aposta Personalizada:** O jogador define o valor da aposta (entre $1 e $100).
- **Simulação de Giro:** Os rolos giram aleatoriamente, exibindo símbolos como A, B, C e D.
- **Verificação de Ganhos:** O jogo verifica se há símbolos alinhados e calcula os ganhos com base nos valores dos símbolos.
- **Balanço Atualizado:** O saldo do jogador é atualizado após cada rodada.
- **Opção de Sair:** O jogador pode sair do jogo a qualquer momento.

## Como Funciona ⚙️

1. **Símbolos e Valores:**
   - Cada símbolo (A, B, C, D) tem uma quantidade específica nos rolos e um valor associado.
   - Quanto mais raro o símbolo, maior o valor do prêmio.

2. **Mecânica do Jogo:**
   - O jogador escolhe o número de linhas e o valor da aposta.
   - Os rolos giram, e os símbolos são exibidos em uma grade 3x3.
   - Se os símbolos em uma linha forem iguais, o jogador ganha um prêmio proporcional ao valor do símbolo e à aposta.

3. **Condições de Vitória:**
   - Os ganhos são calculados apenas para as linhas apostadas.
   - O jogo informa em quais linhas o jogador ganhou e o valor total dos prêmios.

## Por que Este Projeto?
  - Este projeto é ideal para:

  - Aprender conceitos básicos de Python.

  - Entender como funcionam jogos de azar simples.

  - Praticar a lógica de programação e a manipulação de estruturas de dados.

## Divirta-se jogando e sinta-se à vontade para contribuir ou modificar o código! 🚀

## Como Executar ▶️

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/slot-machine-game.git
   
2. Navegue até a Pasta do Projeto
   ```bash
   cd slot-machine-game
   
4. Execute o Jogo
   ```bash
   python mini_project.py
