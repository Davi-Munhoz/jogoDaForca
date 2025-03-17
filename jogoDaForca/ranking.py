def criarArquivo(arquivo):
    '''
    Verifica se existe um arquivo com o nome selecionado e caso não cria um
    :param arquivo: nome do arquivo desejado
    '''
    try:
        with open(arquivo, 'x') as a:
            pass
    except FileExistsError:
        pass


def gravarDados(arquivo, nome, acertos, erros):
    '''
    Grava os dados desejados no arquivo especifico
    :param arquivo: nome do arquivo
    :param nome: nome que será adicionado ao arquivo
    :param acertos: quantidade de acertos no jogo
    :param erros: quantidade de erros cometidos no jogo
    '''
    dados = f"{nome}: {acertos} acertos, {erros} erros"
    try:
        with open(arquivo, 'a') as a:
            a.write(dados + '\n')
    except Exception as e:
        print(f'Erro ao gravar dados: {e}')


def atualizarDados(arquivo, nome, acertos, erros):
    '''
    Caso o  jogador já tenha um registro realiza a atualização dos dados
    :param arquivo: nome do arquivo
    :param nome: nome do jogador
    :param acertos: acertos feitos no jogo
    :param erros: erros cometidos
    '''
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
        usuario_encontrado = False
        for i, linha in enumerate(linhas):
            if nome in linha:
                usuario_encontrado = True
                partes = linha.strip().split(": ")
                dados = partes[1].split(", ")
                acertos_antigos = int(dados[0].split(" ")[0])
                erros_antigos = int(dados[1].split(" ")[0])
                acertos_atualizados = acertos_antigos + acertos
                erros_atualizados = erros_antigos + erros
                linhas[i] = f"{nome}: {acertos_atualizados} acertos, {erros_atualizados} erros\n"
                break
        if not usuario_encontrado:
            linhas.append(f"{nome}: {acertos} acertos, {erros} erros\n")
        with open(arquivo, 'w') as file:
            file.writelines(linhas)
    except Exception as e:
        print(f'Erro ao atualizar dados: {e}')


def mostrarRanking(arquivo):
    '''
    Imprime o ranking atualizado na tela formatado
    :param arquivo: nome do arquivo
    '''
    try:
        with open(arquivo, 'r') as a:
            dados = a.readlines()
        ranking_lista = []
        for linha in dados:
            linha = linha.strip()
            if not linha or ': ' not in linha:
                continue
            nome, acertos_erros = linha.split(': ', 1)
            if ', ' not in acertos_erros:
                continue
            nome, acertos_erros = linha.strip().split(': ')
            acertos, erros = acertos_erros.split(', ')
            acertos = int(acertos.split(' ')[0])
            erros = int(erros.split(' ')[0])
            ranking_lista.append([nome, acertos, erros])
        ranking_lista = sorted(ranking_lista, key=lambda x: x[1], reverse=True)
        print("+------------+--------+----------+--------+")
        print("| Posição   | Nome   | Acertos  | Erros  |")
        print("+------------+--------+----------+--------+")
        for i, (nome, acertos, erros) in enumerate(ranking_lista, 1):
            print("| {0:<10} | {1:<6} | {2:<8} | {3:<6} |".format(i, nome, acertos, erros))
        print("+------------+--------+----------+--------+")
    except Exception as e:
        print(f"Erro ao ler o arquivo de ranking: {e}")