import os
from moviepy.editor import VideoFileClip
from faster_whisper import WhisperModel


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class Audio:
    @staticmethod
    def extrair(video_path: str) -> str:
        """Extrai o áudio de um vídeo e salva em um arquivo."""
        video = VideoFileClip(video_path)

        output_path = os.path.join(PROJECT_DIR, 'transcricoes')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        base_name = os.path.splitext(os.path.basename(video_path))[0]
        audio_path = os.path.join(output_path, f'{base_name}.mp3')
        video.audio.write_audiofile(audio_path)

        print(f'> áudio salvo em: {audio_path}')
        return audio_path

    @staticmethod
    def transcrever(audio_path: str) -> str:
        """Transcreve um arquivo de áudio salvo em audio_path para texto utilizando reconhecimento de fala."""
        print(f">>>>> Transcrevendo áudio: {audio_path}")
        audio_path = audio_path.replace("'", "")
        model = WhisperModel("medium")
        result = model.transcribe(audio_path)

        transcricao = ""
        for segment in result[0]:
            transcricao += segment.text + " "
            
        output_path = os.path.join(PROJECT_DIR, 'transcricoes')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        base_name = os.path.splitext(os.path.basename(audio_path))[0]
        transcricao_path = os.path.join(output_path, f'{base_name}.md')
        with open(transcricao_path, 'w') as f:
            f.write(transcricao.strip())

        print(f'> transcrição salva em: {transcricao_path}')
        return transcricao_path
