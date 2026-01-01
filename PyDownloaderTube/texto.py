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