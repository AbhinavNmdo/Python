import pyttsx3
import speech_recognition
import wikipedia
import pywhatkit
import smtplib
import os
import webbrowser
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>6 and hour<12:
        speak("Good Morning, Abhinav")
    elif hour>12 and hour<17:
        speak("Good Afternoon, Abhinav")
    else:
        speak("Good Evening, Abhinav")

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google('audio', language='en-in')
            print(f"User said {query}\n")
        except Exception as e:
            print("Something is wrong")


if __name__ == '__main__':
    speak("Hello, I am Friday")
    greet()
    takeCommand()