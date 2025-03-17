def multiplayer(arquivo):
    '''
    Pega as informações para o multiplayer e inicializa o jogo com elas
    :param arquivo: nome do arquivo
    '''
    import uteis
    import estilizacao
    import jogo
    estilizacao.cabecalho('MODO MULTIPLAYER')
    jogador1 = uteis.verificaStr('Jogador 1, digite seu nome: ')
    jogador2 = uteis.verificaStr('Jogador 2, digite seu nome: ')
    print(f'\n{jogador1}, você escolherá a palavra que {jogador2} tentará adivinhar.\n')
    cat = uteis.categoria()
    n = uteis.niveis()
    palavra = uteis.palavra(cat, n)
    print(f'\n', {estilizacao.linha()}, '\n')
    print(f'Palavra escolhida! {jogador2}, é a sua vez de jogar!')
    print("="*40 + "\n")
    jogo.jogar(arquivo,jogador2 , categoria=cat, nivel=n, palavra=palavra)

