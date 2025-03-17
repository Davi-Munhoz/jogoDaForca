import ranking
import multiplayer
from estilizacao import cabecalho

def opcoes(opc, arquivo):
    '''
    Verifica a opção escolhida e inicia a função
    :param opc: Opção escolhida
    :param n: Quantidade de digitos
    :param arquivo: nome do arquivo
    '''
    opcoes = {
        1: lambda: jogar(arquivo),
        2: lambda: ranking.mostrarRanking(arquivo),
        3: lambda: multiplayer.multiplayer(arquivo),
        4: lambda: print('Saindo... Obrigado por usar nosso sistema!')
    }
    opcoes.get(opc, lambda: print('\033[31mOpção inválida!\033[m'))()


def cadastro():
    '''
    Realiza o cadastro/loggin de um novo jogador
    :return: nome do jogador
    '''
    from uteis import verificaStr
    cabecalho('CADASTRO/LOGGIN')
    nome = verificaStr('Digite o nome do jogador: ')
    return nome

def jogar(arquivo,nome = None ,categoria=None, nivel=None, palavra=None):
    '''
    Inicializa e realiza o jogo da forca
    :param arquivo: nome do documento com as informações dos jogadores
    :param nome: nome do jogador
    :param categoria: categoria escolhida do jogo
    :param nivel: nivel do jogo
    :param palavra: palavra a ser adivinhada
    '''
    import palavras
    import estilizacao
    import uteis
    from random import choice

    erros = acertos = 0
    if not categoria:
        categoria = uteis.categoria()
    if not nivel:
        nivel = uteis.niveis()
    if not palavra:
        palavra = choice(palavras.palavras[categoria][nivel])
    if not nome:
        nome = cadastro()
    exibicao = ['_'] * len(palavra)
    estilizacao.mostrar_boneco(erros)
    print(' '.join(exibicao))
    palavra_lista = list(palavra)
    tentativas = []
    while erros < 6:
        chute = uteis.verificaStr('Digite uma letra: ')[0]
        if chute in palavra_lista:
            indices = [i for i, letra in enumerate(palavra_lista) if letra == chute]
            print(f'Você acertou! Essa letra está nas posições: {", ".join(map(str, [i + 1 for i in indices]))}!')
            for i in indices:
                exibicao[i] = chute
        else:
            erros += 1
            print(f'\033[31mLetra errada! Você tem {6 - erros} tentativas restantes.\033[m')
            tentativas.append(chute)
        estilizacao.mostrar_boneco(erros)
        print(' '.join(exibicao))
        print(f'Letras já utilizadas: {', '.join(tentativas)}')
        if '_' not in exibicao:
            print('\033[32mPARABÉNS! Você acertou a palavra!\033[m')
            acertos += 1
            if nome in open(arquivo).read():
                ranking.atualizarDados(arquivo, nome, acertos, erros)
            else:
                ranking.gravarDados(arquivo, nome, acertos, erros)
            break
    if erros == 6:
        print(f'\033[31mGAME OVER! A palavra era "{palavra}".\033[m')

