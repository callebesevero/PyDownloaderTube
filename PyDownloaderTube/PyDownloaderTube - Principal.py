from funções import nomeArquivo, mostralistaDeNomes, formatar, título, progressoDownload
from pytubefix import YouTube as yt
from os import path

sufixos = ('Sem sufixo', '(pb)')
opçõesSalvar = ('Áudio', 'Vídeo', 'Áudio e Vídeo')
cont = 0
repetirComandos = 'None'

while True:
    link = str(input('\nInsira a URL [S/SAIR/ENTER para sair] -> ')).strip()

    if link.upper() in 'SAIR':
        break
    elif repetirComandos in 'SIM':
        nome = listaDeNomes[escolhaNome]

        if escolhaSufixo == 0:
            nomeÁudio = nome
            nomeVídeo = nome
        elif escolhaSufixo == 1:
            nomeÁudio = f'{nome} {sufixos[escolhaSufixo]}'
            nomeVídeo = f'{nome} {sufixos[escolhaSufixo]} (vídeo)'
        else:
            nomeÁudio = nomeVídeo = f'{nome} {sufixos[escolhaSufixo]}'
        
        if escolhaPath in 'SIMNÃO' and escolhaPath != '':
            if escolhaPath == 'SIM' or escolhaPath == 'S' and escolhaPath != '':
                pathSalvar = str(input('Insira o caminho da pasta -> ').strip())
                if pathSalvar[0] == '"' and pathSalvar[-1] == '"':
                    pathSalvar = pathSalvar.strip('"')
            elif escolhaPath == 'NÃO' or escolhaPath == 'N' and escolhaPath != '':
                pathSalvar = path.join(path.expanduser('~'), 'Downloads')
    
        if salvar == 0:
            yt(link, on_progress_callback=progressoDownload).streams.get_audio_only().download(output_path=pathSalvar, filename=f'{nomeÁudio}.mp3')
        elif salvar == 1:
            yt(link, on_progress_callback=progressoDownload).streams.get_highest_resolution().download(output_path=pathSalvar, filename=f'{nomeVídeo}.mp4')
        elif salvar == 2:
            yt(link, on_progress_callback=progressoDownload).streams.get_audio_only().download(output_path=pathSalvar, filename=f'{nomeÁudio}.mp3')
            yt(link, on_progress_callback=progressoDownload).streams.get_highest_resolution().download(output_path=pathSalvar, filename=f'{nomeVídeo}.mp4')
        continue
    
    nomeArquivo(link)
    listaDeNomes = mostralistaDeNomes()

    título('ESCOLHA UM DOS NOMES PARA O ARQUIVO', 60, 'amarelo')
    for i, n in enumerate(listaDeNomes):
        if i == 0:
            print(formatar(f'{i} - {n}', 'negrito'))
        else:
            print(f'{i} - {n}')
    escolhaNome = int(input('Insira o índice da opção de nome -> '))
    if escolhaNome == 0:
        nome = str(input('Insira o nome personalizado do arquivo -> ')).strip().title()
    else:
        try:
            nome = listaDeNomes[escolhaNome]
        except:
            print(formatar('Ocorreu um erro ao definir o nome. Insira as informações novamente!', cortexto='vermelho'))
            continue
    
    título('ESCOLHA UM DOS SUFIXOS', 60, 'amarelo')
    for i, suf in enumerate(sufixos):
        if i == 0:
            print(formatar(f'{i} - {suf}', 'negrito'))
        else:
            print(f'{i} - {suf}')
    escolhaSufixo = int(input('Digite o número do sufixo escolhido -> ').strip())
    if escolhaSufixo <= len(sufixos):
        if escolhaSufixo == 0:
            nomeÁudio = nome
            nomeVídeo = nome
        elif escolhaSufixo == 1:
            nomeÁudio = f'{nome} {sufixos[escolhaSufixo]}'
            nomeVídeo = f'{nome} {sufixos[escolhaSufixo]} (vídeo)'
        else:
            nomeÁudio = nomeVídeo = f'{nome} {sufixos[escolhaSufixo]}'


    título('OPÇÕES DE SALVAMENTO', 60, corseparadores='verde')
    for i, opc in enumerate(opçõesSalvar):
        print(f'{i} - {opc}')
    salvar = int(input('Insira a opção de salvamento -> '))

    título('DESEJA SALVAR EM PASTA PERSONALIZADA?', 60, corseparadores='verde')
    escolhaPath = 'None'
    while not escolhaPath in 'SIMNÃO':
        escolhaPath = str(input('[SIM ou S/NÃO ou N] (Se NÃO, será baixado na pasta Downloads) -> ').strip().upper())
        if escolhaPath in 'SIMNÃO' and escolhaPath != '':
            if escolhaPath == 'SIM' or escolhaPath == 'S' and escolhaPath != '':
                pathSalvar = str(input('Insira o caminho da pasta -> ').strip())
                if pathSalvar[0] == '"' and pathSalvar[-1] == '"':
                    pathSalvar = pathSalvar.strip('"')
            elif escolhaPath == 'NÃO' or escolhaPath == 'N' and escolhaPath != '':
                pathSalvar = path.join(path.expanduser('~'), 'Downloads')
            else:
                print('ERRO na sua digitação! Digite, por favor, SIM ou NÃO.')
                escolhaPath = 'None'

    if salvar == 0:
        yt(link, on_progress_callback=progressoDownload).streams.get_audio_only().download(output_path=pathSalvar, filename=f'{nomeÁudio}.mp3')
    elif salvar == 1:
        yt(link, on_progress_callback=progressoDownload).streams.get_highest_resolution().download(output_path=pathSalvar, filename=f'{nomeVídeo}.mp4')
    elif salvar == 2:
        yt(link, on_progress_callback=progressoDownload).streams.get_audio_only().download(output_path=pathSalvar, filename=f'{nomeÁudio}.mp3')
        yt(link, on_progress_callback=progressoDownload).streams.get_highest_resolution().download(output_path=pathSalvar, filename=f'{nomeVídeo}.mp4')
    
    if cont == 0:
        repetirComandos = 'None'
        while repetirComandos == 'None':
            repetirComandos = str(input('Deseja repetir os comandos para os próximos arquivos? [SIM ou S/NÃO ou N] -> ').strip().upper())
            if repetirComandos == 'SIM' or repetirComandos == 'S' and repetirComandos != '':
                ...
            elif repetirComandos == 'NÃO' or repetirComandos == 'N' and repetirComandos != '':
                ...
            else:
                repetirComandos = 'None'
                print('Opção inválida! Digite novamente.')
    cont = 1