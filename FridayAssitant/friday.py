import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import smtplib
import os
import webbrowser
import pyaudio
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
        speak("Good Morning, Abheenav")
    elif hour>12 and hour<17:
        speak("Good Afternoon, Abheenav")
    else:
        speak("Good Evening, Abheenav")

def fridayCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say F.R.I.D.A.Y to activate")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            reco = r.recognize_google(audio, language='en-in')
            speak("yes")
        except Exception as e:
            print(e)
        return reco

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            reco1 = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Something is wrong")
            print(e)
        return reco1


if __name__ == '__main__':
    speak("Hello, I am Friday")
    # greet()
    while True:
        try:
            command = fridayCommand().lower()
            if 'friday' in command:
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    speak("Searching Wikipedia...")
                    print("Searching Wikipedia...")
                    query1 = query.replace("wikipedia", "")
                    result = wikipedia.summary(query1, sentences=2)
                    speak("According to wikipedia.")
                    print(f"In Wikipedia: {result}")
                    speak(result)

                elif 'search on youtube' in query:
                    speak("Searching in youtube")
                    query1 = query.replace("search on youtube", "")
                    result = pywhatkit.playonyt(query1)
                    speak("Here is the results")

                elif 'search on google' in query:
                    speak("Searching on google")
                    print("Searching on google")
                    query1 = query.replace("search on Google", "")
                    google = pywhatkit.search(query1)
                    speak("Here is the results")

                elif 'play music on youtube' in query:
                    speak("Searching on youtube")
                    query1 = query.replace("play music on youtube", "")
                    result = pywhatkit.playonyt(query1)
                    speak("Here is the results")

                elif 'tell me about' in query:
                    speak('ok searching')
                    query1 = query.replace("tell me about", "")
                    speak("here is the results")
                    result = pywhatkit.info(query1, lines=4)

                elif 'thanks' in query:
                    speak("Welcome sir")

                elif 'tell me a joke' in query:
                    joke = pyjokes.get_jokes()
                    speak("joke")

                elif 'kya kar rahe ho' in query:
                    speak("tumhae kyae krnaa")

                else:
                    print("Something is wrong in query")
                    speak("Something wrong in query")


        except Exception as e:
            speak("got exception")
            print(e)
