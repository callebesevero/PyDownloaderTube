from pytubefix import YouTube as yt
listaDeNomes = list()


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

    
def retornalistaDeNomes():
    return listaDeNomes