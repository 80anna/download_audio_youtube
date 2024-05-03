from pytube import YouTube
from moviepy.editor import *

def download_audio(link):
    try:
        # download
        link_video = YouTube(link)
        video_titulo = link_video.title
        audio_video = link_video.streams.filter(only_audio=True).first()
        print("Baixando áudio de:", video_titulo)
        audio_video.download(filename='temp.mp4')
        audio_arquivo = AudioFileClip('temp.mp4')
        
        # conversao para mp3
        audio_arquivo.write_audiofile(f'{video_titulo}.mp3')
        audio_arquivo.close()
        os.remove('temp.mp4')
        print("Download do áudio completo!")
        
    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == "__main__":
    link = input("Insira o link do vídeo do YouTube: ")
    download_audio(link)


