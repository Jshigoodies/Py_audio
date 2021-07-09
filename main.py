import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

from browser_websites import Browser


class MainSetUp:
    def __init__(self):
        self.browser = Browser()

    @staticmethod
    def speak(text):
        tts = gTTS(text=text, lang="en")  # transform text into a aduio file in the language of english
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    @staticmethod
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""
            try:
                said = r.recognize_google(audio)
            except Exception as e:
                print("Could not hear")

        return said

    @staticmethod
    def list_of_microphones():
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
