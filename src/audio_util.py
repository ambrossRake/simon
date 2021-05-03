import wave
import pyaudio
from pydub import AudioSegment

class AudioTools:

    __instance = None

    @staticmethod
    def getInstance():
        if AudioTools.__instance == None:
            AudioTools()
        return AudioTools.__instance

    def __init__(self):
        if AudioTools.__instance != None:
            raise Excetion('There is already an instance of AudioTools, please use getInstance()')
        else:
            self.currently_playing_audio = None
            self.wave_form = None
            self.py_audio = pyaudio.PyAudio()
            AudioTools.__instance = self

    def __audio_callback(self, data, frame_count, time_info, status):
        #print(time_info)
    #    print(status)
        data = self.wave_form.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def play_audio(self, path): #assumes mp3 file
        audio = AudioSegment.from_mp3(path)
        export_path = '../res/audio.wav'
        audio.export(export_path, format='wav')
        self.wave_form = wave.open(export_path, 'rb')
        self.currently_playing_audio = self.py_audio.open(format=self.py_audio.get_format_from_width(self.wave_form.getsampwidth()),
                                                channels=self.wave_form.getnchannels(),
                                                rate=self.wave_form.getframerate(),
                                                output=True,
                                                stream_callback=self.__audio_callback)
        self.currently_playing_audio.start_stream()

    def stop_audio(self):
        self.currently_playing_audio.stop_stream()
        self.currently_playing_audio.close()
        self.wave_form.close()
        self.py_audio.terminate() #should be called when program exits

    def pause_audio(self):
        self.currently_playing_audio.stop_stream()

    def resume_audio(self):
        self.currently_playing_audio.start_stream()
