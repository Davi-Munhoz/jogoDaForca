import uteis
from jogo import opcoes
from ranking import criarArquivo

while True:
    pontuacao = 'ranking.txt'
    criarArquivo(pontuacao)
    opcao = uteis.menu()
    opcoes(opcao, pontuacao)
    if opcao == 4:
        break