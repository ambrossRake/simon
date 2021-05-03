import youtube_dl
from audio_util import AudioTools

from command import Command
class PlayCommand(Command):

    def __init__(self):
        super().__init__("Play", "Plays the first track matching the given keywords from youtube", self.play, None)

    def play(self, keywords):
        print(keywords)

        ydl_options = {
            'format': 'bestaudio/best',
            'outtmpl': '../res/temp_audio.m4a',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            result = ydl.download(['ytsearch:'+keywords])

#            result = ydl.extract_info('ytsearch:'+keywords, download = True)
        AudioTools.getInstance().play_audio('../res/temp_audio.mp3')
