from pytubefix import YouTube as yt
listaDeNomes = list()


def formatar(mensagem, formatação='nenhuma', cortexto='nenhuma', corfundo='nenhuma'):
    dic_formatação = {'nenhuma': '0',
                      'negrito': '1',
                      'sublinhado': '4',
                      'negativo': '7'}
    dic_corestexto = {'nenhuma': '',
                      'preto': '30',
                      'vermelho': '31',
                      'verde': '32',
                      'amarelo': '33',
                      'azul': '34',
                      'magenta': '35',
                      'ciano': '36',
                      'cinza claro': '37'}
    dic_coresfundo = {'nenhuma': '',
                      'preto': '40',
                      'vermelho': '41',
                      'verde': '42',
                      'amarelo': '43',
                      'azul': '44',
                      'magenta': '45',
                      'ciano': '46',
                      'cinza claro': '47'}
    
    if cortexto == corfundo == 'nenhuma':
        início = '\033[' + dic_formatação[formatação] + 'm'
    elif corfundo == 'nenhuma':
        início = '\033[' + dic_formatação[formatação] + ';' + dic_corestexto[cortexto] + 'm'
    else:
        início = '\033[' + dic_formatação[formatação] + ';' + dic_corestexto[cortexto] + ';' + dic_coresfundo[corfundo] + 'm'
    fim = "\033[m"
    return f"{início}{mensagem}{fim}"


def título(mensagem, tamanho=20, corseparadores='nenhuma'):
    if corseparadores == 'nenhuma':
        print()
        print(f'{"-"*tamanho}')
        print(f'{f"{mensagem}".center(tamanho)}')
        print(f'{"-"*tamanho}')
    else:
        print()
        print(f'{formatar("-", cortexto=corseparadores)*tamanho}')
        print(f'{f"{formatar(mensagem, cortexto=corseparadores)}".center(tamanho)}')
        print(f'{formatar("-", cortexto=corseparadores)*tamanho}')


def nomeArquivo(link):
    listaDeNomes.clear()
    listaDeNomes.append('Escolha personalizada')

    nome = str(yt(link).title).title()
    listaDeNomes.append(nome)
    nomeFracionado = nome.split()

    índicesSeparadores = [0]
    for separador in '–-|/':
        if separador in nomeFracionado:
            cont = 0
            while True:
                if cont == 0:
                    índicesSeparadores.append(nomeFracionado.index(separador))
                else:
                    try:
                        índiceSeparador = nomeFracionado[índicesSeparadores[cont+1]:].index(separador)
                        if not índiceSeparador in índicesSeparadores:
                            índicesSeparadores.append(índiceSeparador)
                    except:
                        break
                índicesSeparadores.sort()
                cont += 1
    interv = 0
    interv2 = 1
    for _ in range(len(índicesSeparadores)):
        if _ != len(índicesSeparadores) - 1:
            if _ == 0:
                listaDeNomes.append(' '.join(nomeFracionado[índicesSeparadores[interv]:índicesSeparadores[interv2]]))
            else:
                listaDeNomes.append(' '.join(nomeFracionado[índicesSeparadores[interv] + 1:índicesSeparadores[interv2]])) # + 1 é para não captar o separador
        else:
            listaDeNomes.append(' '.join(nomeFracionado[índicesSeparadores[interv] + 1:])) # + 1 é para não captar o separador
        interv += 1
        interv2 += 1

    if len(índicesSeparadores) == 1:
        for t in nomeFracionado:
            if len(t) > 4:
                listaDeNomes.append(t)
            listaDeNomes.append(' '.join(nomeFracionado[nomeFracionado.index(t):]))

    
def mostralistaDeNomes():
    return listaDeNomes


def progressoDownload(stream, bytes, tamanhoFaltando):
    tamanhoTotal = stream.filesize
    tamanhoBaixado = tamanhoTotal - tamanhoFaltando
    porcentagem = (tamanhoBaixado / tamanhoTotal) * 100
    barrinha = f'{int(porcentagem) * "▮"}{(100 - int(porcentagem)) * "."}'
    
    print(f'\rA baixar {barrinha}   {porcentagem:.1f}%', end='', flush=True)
    if tamanhoTotal == tamanhoBaixado:
        print()