from Texto import título, formatar


def escolhaNome(listaDeNomes):
    título('ESCOLHA UM DOS NOMES PARA O ARQUIVO', 60)
    for i, n in enumerate(listaDeNomes):
        if i == 0:
            print(formatar(f'{i} - {n}', 'negrito'))
        else:
            print(f'{i} - {n}')


def escolhaSufixo(sufixos):
    título('ESCOLHA UM DOS SUFIXOS', 60)
    for i, suf in enumerate(sufixos):
        if i == 0:
            print(formatar(f'{i} - {suf}', 'negrito'))
        else:
            print(f'{i} - {suf}')

    
def opçõesSalvamento(opçõesSalvar):
    título('OPÇÕES DE SALVAMENTO', 60, corseparadores='verde')
    for i, opc in enumerate(opçõesSalvar):
        print(f'{i} - {opc}')