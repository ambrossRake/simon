import speech_recognition as sr
from playsound import playsound
from command import Command
from play_command import PlayCommand
from stop_command import StopCommand
import time

recognizer = sr.Recognizer()
activation_phrase = 'simon'
commands = [PlayCommand(), StopCommand()]

def on_phrase_predicted(recognizer, audio):
    try:
        speech_prediction = recognizer.recognize_sphinx(audio)
        print("Prediction: " + speech_prediction)
        if(activation_phrase in speech_prediction):
            playsound('../res/activation_audio.wav')
            for command in commands:
                if(command.name.lower() in speech_prediction):
                    try:
                        command.execute(speech_prediction[6+len(command.name)+1:])
                    except:
                        print("An error occured while executing command: " + command.name )
    except sr.UnknownValueError:
        print("Could not understand audio") #TODO Add actual logging..
    except sr.RequestError as err:
        print("Sphinx error: {0}".format(err))

def main():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise")
        recognizer.adjust_for_ambient_noise(source)

    stop_listening = recognizer.listen_in_background(sr.Microphone(), on_phrase_predicted)
    time.sleep(1000)

if __name__ == '__main__':
    main()
