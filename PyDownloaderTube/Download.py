def progressoDownload(
    stream, 
    bytes, 
    tamanhoFaltando
):
    tamanhoTotal = stream.filesize
    tamanhoBaixado = tamanhoTotal - tamanhoFaltando
    porcentagem = (tamanhoBaixado / tamanhoTotal) * 100
    barrinha = f'{int(porcentagem) * "▮"}{(100 - int(porcentagem)) * "."}'
    
    print(f'\rA baixar {barrinha}   {porcentagem:.1f}%', end='', flush=True)
    if tamanhoTotal == tamanhoBaixado:
        print()


def download(
        link, 
        pathSalvar, 
        salvar, 
        nomes
):
    
    from pytubefix import YouTube as yt

    nomeÁudio = nomes[0]
    nomeVídeo = nomes[1]
    # Áudio
    if salvar == 0:
        yt(link, on_progress_callback=progressoDownload).streams.get_audio_only().download(output_path=pathSalvar, filename=nomeÁudio)
    # Vídeo
    elif salvar == 1:
        yt(link, on_progress_callback=progressoDownload).streams.get_highest_resolution().download(output_path=pathSalvar, filename=nomeVídeo)
    # Áudio e vídeo
    elif salvar == 2:
        yt(link, on_progress_callback=progressoDownload).streams.get_audio_only().download(output_path=pathSalvar, filename=nomeÁudio)
        yt(link, on_progress_callback=progressoDownload).streams.get_highest_resolution().download(output_path=pathSalvar, filename=nomeVídeo)


def converter(
        pathSalvar: str, 
        nomeÁudio: str
):
    from pydub import AudioSegment

    # AudioSegment.converter = r"C:\Users\Lean\.ffmpeg\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe"
    # AudioSegment.ffprobe = r"C:\Users\Lean\.ffmpeg\ffmpeg-8.0.1-essentials_build\bin\ffprobe.exe"

    pathÁudio = rf'{pathSalvar}\{nomeÁudio}'
    áudio = AudioSegment.from_file(pathÁudio)
    
    nomeNovoÁudio = nomeÁudio.replace('m4a', 'mp3')
    pathNovoÁudio = rf'{pathSalvar}\{nomeNovoÁudio}'
    áudio.export(out_f=pathNovoÁudio, format='mp3', bitrate='320k')