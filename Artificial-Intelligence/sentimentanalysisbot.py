from textblob import TextBlob
from dataclasses import dataclass

@dataclass

class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text : str, *, threshold: float) -> Mood:
    sentiment = TextBlob(input_text).sentiment.polarity 
    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold
    
    if sentiment >= friendly_threshold:
        return Mood(":)", sentiment)
    elif sentiment < hostile_threshold:
        return Mood(":,(", sentiment)
    else:
        return Mood(":\\", sentiment)

def send_resources(mood : Mood):
    if mood.emoji == ':)':
        print("I am happy to hear that, hope you have a lovely rest of your day!")
    elif mood.emoji == ':,(':
        print("I’m sorry to hear that. Here are some resources that might help: ")
        print("- Mental Health Helpline: https://cmha.ca/find-info/mental-health/general-info/")
        print("Stay strong!")
    else:
        print("It seems like you're feeling neutral. Take it easy and take care!")

if __name__ == '_main_':
    while True:
        text: str = input('How are you feeling today ? : ')
        mood: Mood = get_mood(text, threshold=0.3)
        send_resources(mood)