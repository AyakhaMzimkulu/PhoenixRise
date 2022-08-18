import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

find_my_ip()

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

search_on_wikipedia()

def play_on_youtube(video):
    kit.playonyt(video)
    
play_on_youtube()

def search_on_google(query):
    kit.search(query)

search_on_google()

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

def send_email(reciever_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = reciever_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

def get_random_joke():
    headers = {
        'Accept' : 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']