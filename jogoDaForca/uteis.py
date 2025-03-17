from estilizacao import cabecalho

def verificaInt(msg):
    '''
    Solicita um número e verifica se foi digitado um número inteiro
    :param msg: Mensagem de solicitação
    :return: O número digitado
    '''
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[31mDigite um número inteiro dentro das opções! \033[m')
        else:
            return n


def verificaStr(msg):
    '''
        Solicita uma letra/palavra e verifica se foi digitado um valor válido
        :param msg: Mensagem de solicitação
        :return: Letra/palavra digitada
        '''
    while True:
        try:
            p = str(input(msg)).strip().lower()
            if len(p) == 0 or not p.isalpha():
                raise ValueError
        except ValueError:
            print('\033[31mDigite uma palavra/letra válida! \033[m')
        else:
            return p


def menu():
    '''
    Menu com as opções do jogo
    '''
    from estilizacao import cabecalho
    cabecalho('MENU')
    print('''\n1- Jogar
2- Ranking
3- Modo Multiplayer
4- Sair''')
    while True:
        opc = verificaInt('Escolha sua opção: ')
        if opc < 0 or opc > 4:
            print('\033[31mOpção inválida! Tente novamente.\033[m')
        else:
            break
    return opc

def categoria():
    '''
    Faz a seleção da categoria com base no dicionario já criado
    :return: a categoria escolhida
    '''
    cabecalho('CATEGORIAS')
    opcoes = ['animais', 'profissões', 'frutas', 'objetos']
    for i, cat in enumerate(opcoes, 1):
        print(f'{i}º {cat}')
    while True:
        escolha = verificaInt('Digite sua escolha: ')
        if 1 <= escolha <= len(opcoes):
            return opcoes[escolha-1]
        print('\033[31mOpção inválida! Tente novamente\033[m')

def niveis():
    '''
    Faz a seleção do nivel com base no dicionario já criado
    :return: o nivel escolhida
    '''
    cabecalho('NIVEIS')
    opcoes = ['fácil', 'médio', 'difícil']
    for i, n in enumerate(opcoes, 1):
        print(f'{i}º {n}')
    while True:
        nivel = verificaInt('Digite sua escolha: ')
        if 1 <= nivel <= len(opcoes):
            return opcoes[nivel-1]
        print('\033[31mOpção inválida! Tente novamente\033[m')

def palavra(cat, n):
    '''
        Faz a seleção da palavra com base no dicionario já criado
        :return: a palavra escolhida
        '''
    from palavras import palavras
    cabecalho('PALAVRAS')
    for i, valor in enumerate(palavras[cat][n], 1):
        print(f'{i}º {valor}')
    p = verificaInt('Digite o númeor da sua escolha: ')
    return palavras[cat][n][p-1]
