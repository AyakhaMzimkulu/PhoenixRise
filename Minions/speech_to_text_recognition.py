import speech_recognition as sr
import pyttsx3

#Init of the recognizer
r = sr.Recognizer()

#function to convert text to speech

def SpeakText(command):
    #init the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
    
#using microphone as source for input

with sr.Microphone() as source2:
    
            #wiat a sec & let recongniser adjust the energy threshold based on surrounding noise level
    r.adjust_for_ambient_noise(source2, duration=0.2)
    
            #listens for users input
    audio2 = r.listen(source2)
    
            #use google to recognise audio
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
    
    print("Did you say " +MyText)         