# elotte dependecies:
"""pip install speechrecognition
pip install pyttsx3  for offline usage
pip install pyaudio  if (If there is a issue in installing PyAudio use .whl file from this link https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
pip install playsound
pip install PyObjC """

import speech_recognition as sr  # recognise speec
import time
import sys
from os import curdir, path
from src import email

baseF = path.abspath(curdir)
EMAILCIMFAJL = path.join(baseF, "hangdetektalos\\voicerec_env\\src\\emailCimek.csv")


r = sr.Recognizer()  # initialise a recogniser
valasz_var = [
    "Segíthetek?",
    "Mondtál valamit?",
    "Nem biztos, hogy hallom, amit mondasz...",
    "Türelem, türelem...",
    "Megszólalsz még ma?",
]


def language_choose(ask=""):
    languages = ["english", "magyar"]
    select = input(ask).lower()
    if select == languages[0]:
        return "en-US"
    else:
        return "hu-HU"


# listen for audio and convert it to text:
def record_audio(ask="", language="en-US"):
    if language == "en-US":
        time.sleep(1)
        while 1:
            record_audio_eng()
    else:
        time.sleep(1)
        while 1:
            record_audio_hun()


# if i want to use it again, withut language selection:
def record_audio_eng(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            print(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            print("I did not get that")
        except sr.RequestError:
            print("Sorry, the service is down")  # error: recognizer is not connected

            # print what user said
        respond(voice_data.lower())
        return voice_data.lower()


def record_audio_hun(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            print(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Miben segíthetek?")
        voice_data = ""
        try:
            voice_data = r.recognize_google(
                audio, language="hu-HU"
            )  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            print("Nem értem, beszéljé magyarul!!")
        except sr.RequestError:
            print("Bocsika, a szolgáltatás off:(")  # error: recognizer is not connected

            # print what user said
        respond(voice_data.lower())
        return voice_data.lower()


def email_beolvas(EMAILCIMFAJL):
    emailcimek = []
    with open(EMAILCIMFAJL, "r+", encoding="utf-8") as f:
        for cim in f:
            cim = cim.strip().split(";")
            emailcimek.append(email.Email(cim[0], cim[1], cim[2]))
    return emailcimek


def respond(voice_data):
    kilep = ["exit", "quit", "kilépés", "kilép"]
    keres = ["keresés", "search", "look up", "keress"]
    mailcímek = [
        "lokolobo",
        "skybluereka",
        "szkájblúréka",
        "vorosnadrag",
    ]
    for i in range(len(kilep)):
        if kilep[i] in voice_data:
            print("Najó, én feladtam...")
            print("Good Bye!!")
            sys.exit()

    for i in range(len(keres)):
        if keres[i] in voice_data:
            if keres[i] == "keress" or keres[i] == "keres" or keres[i] == "keresés":
                record_audio_hun("Miről szeretnél több információt megtudni?")
            else:
                record_audio_eng("What do you want to search for?")
            open_google()


def open_google():
    url = "https://www.google.com/"
    pass


emailFiokok=email_beolvas(EMAILCIMFAJL)
