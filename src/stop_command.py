from audio_util import AudioTools
from command import Command
class StopCommand(Command):

    def __init__(self):
        super().__init__("Stop", "Stops currently playing track", self.stop, None)

    def stop(self, args):
        AudioTools.getInstance().stop_audio()
