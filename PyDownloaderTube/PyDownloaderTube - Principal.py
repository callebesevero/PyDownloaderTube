from os import path
from pathlib import WindowsPath
from Funções import nomeArquivo, retornalistaDeNomes
from Texto import formatar, título
import Sufixo
import Mostra
import Download

sufixos = ('Sem sufixo', '(pb)')
opçõesSalvar = ('Áudio', 'Vídeo', 'Áudio e Vídeo')
cont = 0
repetirComandos = 'None'

while True:
    link = str(input('\nInsira a URL [S/SAIR/ENTER para sair] -> ')).strip()

    if link.upper() in 'SAIR':
        break
    elif repetirComandos in 'SIM':
        nomeArquivo(link)
        listaDeNomes = retornalistaDeNomes()
        nome = listaDeNomes[escolhaNome]

        nomes = Sufixo.nomeSufixo(sufixos, nome, escolhaSufixo)

        Download.download(link, pathSalvar, salvar, nomes)
        continue
    
    # Principal
    nomeArquivo(link)
    listaDeNomes = retornalistaDeNomes()

    Mostra.escolhaNome(listaDeNomes)
    escolhaNome = int(input('Insira o índice da opção de nome -> '))
    if escolhaNome == 0:
        nome = str(input('Insira o nome personalizado do arquivo -> ')).strip().title()
    else:
        try:
            nome = listaDeNomes[escolhaNome]
        except:
            print(formatar('Ocorreu um erro ao definir o nome. Insira as informações novamente!', cortexto='vermelho'))
            continue
    
    Mostra.escolhaSufixo(sufixos)
    escolhaSufixo = int(input('Digite o número do sufixo escolhido -> ').strip())
    nomes = Sufixo.nomeSufixo(sufixos, nome, escolhaSufixo)
    nomeÁudio = nomes[0]
    nomeVídeo = nomes[1]

    Mostra.opçõesSalvamento(opçõesSalvar)
    salvar = int(input('Insira a opção de salvamento -> '))

    título('PASTA PERSONALIZADA', 60)
    escolhaPath = 'None'
    while not escolhaPath in 'SIMNÃO':
        escolhaPath = str(input('Salvar em pasta personalizada? [SIM ou S/NÃO ou N] (Se NÃO, será baixado na pasta Downloads) -> ').strip().upper())
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

    Download.download(link, pathSalvar, salvar, nomes)
    
    # Convertendo m4a para mp3
    if salvar == 0 or salvar == 2:
        Download.converter(pathSalvar, nomeÁudio)

    if cont == 0:
        repetirComandos = 'None'
        while repetirComandos == 'None':
            repetirComandos = str(input('Deseja repetir os comandos para os próximos arquivos? [SIM ou S/NÃO ou N] -> ').strip().upper())
            if not repetirComandos == 'SIM' and not repetirComandos == 'S' and not repetirComandos == 'NÃO' and not repetirComandos == 'N':
                repetirComandos = 'None'
                print('Opção inválida! Digite novamente.')
        cont = 1