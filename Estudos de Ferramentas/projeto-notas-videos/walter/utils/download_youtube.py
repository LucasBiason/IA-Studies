import os
import re
from pytubefix import YouTube


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class YoutubeDownloader:
    
    @staticmethod
    def baixar_video(link=''):
        print(f">>>>> Baixando vídeo do link: {link}")
        yt = YouTube(link, 'WEB')
        titulo = yt.title
        stream = yt.streams.get_highest_resolution()

        output_path = os.path.join(PROJECT_DIR, 'transcricoes', '_videos')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        title = re.sub(r'[<>:"/\\|?*]', '', titulo)
        title = title.replace("'", "")
        title = title.strip().replace(' ', '_')
        title = f'_{title}.mp4'
        video_path = stream.download(output_path, title)
        print(f"> Baixado vídeo '{titulo}' para '{video_path}'")
        video_path = f'{output_path}/{title}'
        print(f"> Vídeo baixado em: {video_path}")
        return video_path

