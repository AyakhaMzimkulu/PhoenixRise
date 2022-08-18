from email import header
from ipaddress import ip_address
from urllib import request
import pyttsx3
import datetime
import speech_recognition as sr
import os
import subprocess as sp


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
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
    


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
    

def wishme():
    speak("Welcome back sir!")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour = datetime.datetime.now().hour
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

paths = {
    'notepad' : "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord' : "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator' : "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:' , shell=True)
    
open_camera()

    
def open_notepad():
    os.startfile(paths['notepad'])

open_notepad()

    
def open_discord():
    os.startfile(paths['discord'])

open_discord()

    
def open_cmd():
    os.system('start cmd')

open_cmd()

    
def open_calculator():
    sp.Popen(paths['calculator'])

open_calculator()

