from datetime import datetime
import pyttsx3
from decouple import config
import speech_recognition as sr
from utils import opening_text

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init()

engine.setProperty('rate' , 200)
engine.setProperty('volume' , 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak("this is Drake ai assistant")

def time():
    Time = datetime.now().strftime("%I:%M:%S")
    speak(Time)
    


def date():
    year = int(datetime.now().year)
    month = int(datetime.now().month)
    date = int(datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
    

def wishme():
    speak("Welcome back sir!")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour = datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morining sir!")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour <24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
        
    speak("How may I be of assistance today?")
    
wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uk')
        print(query)

    except Exception as e:
        print(e)
        speak("I'm sorry, I did not understand. Could you repeat that again please?")
        
        
        return "None"
    return query

takeCommand()