import pyttsx3 #pip install pyttsx3 == text data into speech
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        
        speak("Hello this is Otto")
        
        def time():
            Time = datetime.datetime.now().strftime("%I:%M:%S") #hour = i minutes = m seconds = s
            speak("the current time is:")
            speak(Time)
        time()
#while True:
#    voice = int(input("Press 1 for male voice\nPress 2 for female voice"))
#    speak(audio)
#getvoices(voice)