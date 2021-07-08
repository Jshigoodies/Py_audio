import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

from browser_websites import Browser

def speak(text):
    tts = gTTS(text=text, lang="en")  # transform text into a aduio file in the language of english
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


def list_of_microphones():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


# Runner
browser = Browser()

speak("hello Jshi")
# list_of_microphones()
text = get_audio()

if "Google" in text:
    speak("you said google")
    browser.google()
if "good" in text:
    speak("you said good")