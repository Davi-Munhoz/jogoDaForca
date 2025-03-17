# Jogo da Forca
Este projeto é uma implementação do clássico Jogo da Forca, desenvolvido totalmente em Python, com diversas categorias, dificuldades e suporte para os modos multiplayer e singleplayer.

## Funcionalidades
Criação e atualização de cadastro de jogadores
Escolha de categorias e níveis de dificuldade
Registro de estatísticas de cada jogador (acertos e erros)
Exibição gráfica do boneco da forca
Armazenamento do ranking em um arquivo .txt
## Como usar
### Requisitos
Python 3.x
Biblioteca random (já incluída na instalação padrão do Python)
### Passos para rodar o projeto
1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/jogo-da-forca.git
2. Acesse o diretório do projeto:
    ```bash
    cd jogo-da-forca
3. Execute o jogo:
    ```bash
    python main.py
4. O sistema perguntará:
  - O que você deseja fazer:
    
      1- Jogar
    
      2- Modo Multiplayer
    
      3- Ver Ranking
    
      4- Sair
    
  - Se escolher Jogar ou Modo Multiplayer, o sistema solicitará o(s) nome(s) do(s) jogador(es).
  - A categoria desejada entre:
    
      1- Animais
    
      2- Profissões
    
      3- Frutas
    
      4- Objetos
    
  - O nível de dificuldade:
    
      1- Fácil
    
      2- Médio
    
      3- Difícil
  - No modo multiplayer, um jogador escolherá a palavra para o outro adivinhar.
5. O jogo será gerado conforme as opções escolhidas.
## Como funciona
- O projeto utiliza a biblioteca random para escolher uma palavra de um dicionário pré-definido.
- As palavras estão organizadas por categoria e nível de dificuldade.
- O usuário escolhe a categoria e o nível desejado.
- O jogo exibe a palavra oculta e permite que o jogador tente adivinhar as letras.
- Os dados gerados (acertos e erros) são registrados no arquivo de ranking associado ao nome do jogador.
- Um ranking geral pode ser acessado no menu principal.
## Estrutura do projeto
jogo_da_forca

│-- 📄 main.py           # Arquivo principal para execução do jogo

│-- 📄 palavras.py       # Lista de palavras organizadas por categoria e dificuldade

│-- 📄 estilizacao.py    # Funções de exibição e estilização do jogo

│-- 📄 uteis.py          # Funções auxiliares

│-- 📄 ranking.py        # Gerenciamento de ranking e estatísticas dos jogadores

│-- 📄 multiplayer.py    # Implementação do modo multiplayer

│-- 📄 README.md         # Documentação do projeto


## Melhorias futuras
- Interface gráfica
- Banco de dados para armazenamento de jogadores
- Implementação de um manual de instruções
## Licença
Este projeto está licenciado sob a **MIT License**.
