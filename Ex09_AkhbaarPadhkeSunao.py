import json

import requests


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    print("Speaking.....")
    speak.Speak(str)

if __name__ == '__main__':
    url = "https://newsapi.org/v2/top-headlines?category=science&apiKey=33e7205e2fe547089f0fe1cb9e41f4bc"
    news = requests.get(url).text
    news_json = json.loads(news)
    print(news_json["status"])
    arts = news_json["articles"]
    speak("News for today")
    for article in arts:
        speak(article["title"])
        speak("Next news")

