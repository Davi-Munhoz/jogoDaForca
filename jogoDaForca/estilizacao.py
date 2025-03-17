tam = 10

def cabecalho(msg):
    '''
    Faz um cabeçaho organizado
    :param msg: mensagem que irá no centro do cabeçalho
    :return:
    '''
    print('\n')
    print('='*tam, msg, '='*tam)

def linha():
    '''
    Uma linha para design
    '''
    print('===='*tam)


def mostrar_boneco(tentativas_erradas):
    '''
    Imprime o boneco do jogo da forca de acordo com seus erros no jogo
    :param tentativas_erradas: erros cometidos no jogo
    '''
    boneco = [
        '''
         -----
         |   |
             |
             |
             |
             |
            ---
        ''',
        '''
         -----
         |   |
         O   |
             |
             |
             |
            ---
        ''',
        '''
         -----
         |   |
         O   |
         |   |
             |
             |
            ---
        ''',
        '''
         -----
         |   |
         O   |
        /|   |
             |
             |
            ---
        ''',
        '''
         -----
         |   |
         O   |
        /|\  |
             |
             |
            ---
        ''',
        '''
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
            ---
        ''',
        '''
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
            ---
        '''
    ]
    print(boneco[tentativas_erradas])