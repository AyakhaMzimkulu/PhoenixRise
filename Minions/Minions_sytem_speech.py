import pyttsx3  # pip install pyttsx3 == text data into speech

engine = pyttsx3.init()

engine.say('Hello, this is Drake, How may I be of assistance?')
engine.runAndWait()
