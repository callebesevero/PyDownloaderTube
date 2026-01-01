def nomeSufixo(sufixos, nome, escolhaSufixo):
    if escolhaSufixo <= len(sufixos):
        if escolhaSufixo == 0:
            nomeÁudio = f'{nome}.m4a'
            nomeVídeo = f'{nome}.mp4'
        elif escolhaSufixo == 1:
            nomeÁudio = f'{nome} {sufixos[escolhaSufixo]}.m4a'
            nomeVídeo = f'{nome} {sufixos[escolhaSufixo]} (vídeo).mp4'
        else:
            nomeÁudio = f'{nome} {sufixos[escolhaSufixo]}.mp3'
            nomeVídeo = f'{nome} {sufixos[escolhaSufixo]}.mp4'
    return (nomeÁudio, nomeVídeo)