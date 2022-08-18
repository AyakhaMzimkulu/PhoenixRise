from ipaddress import ip_address
import requests
from functions.speech import takeCommand, wishme
from functions.speech import speak
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email
from functions.os_ops import open_calculator, open_camera, open_cmd, open_discord, open_notepad,  open_discord
from pprint import pprint

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'open notepad' in query or 'notes' in query:
            open_notepad()
            
        elif 'open discord' in query:
            open_notepad()
            
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
            
        elif 'open camera' in query:
            open_camera()
            
        elif 'open calculator' in query:
            open_calculator()
            
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on your screen.')
            print(f'Your IP Address is {ip_address}')
            
        elif 'wikipedia' in query:
            speak('What would you like to search on Wikipedia?')
            search_query = takeCommand().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For you covenience, I am printing it on your screen.")
            print(results)
            
        elif 'youtube' in query:
            speak('What would you like to play?')
            video = takeCommand().lower()
            play_on_youtube(video)
            
        elif 'search on google' in query or 'google' in query:
            speak('What would you like to search?')
            query = takeCommand().lower()
            search_on_google(query)
            
        elif "send an email" in query or "email"in query:
            speak("To what email address do I send it to? Please enter it in the console: ")
            reciever_address = input("Enter email address: ")
            speak("What should the subject be?")
            subject = takeCommand().capitalize()
            speak("And what is the message?")
            message = takeCommand().capitalize()
            if send_email(reciever_address, subject, message):
                speak("Email sent.")
            else:
                speak("Something went wrong while sending the email. Please check the error logs.")
                
        elif 'joke' in query:
            speak(f"Get a load of this, LOL.")
            joke = get_random_joke()
            speak(joke)
            speak("I hope that cheered you up. For your convenience, I am printing it on your screen.")
            pprint(joke)
            
        elif 'advice' in query:
            speak(f"There is a wise saying that says")
            advice = get_random_advice()
            speak(advice)
            speak("Now that's wise words if you ask me.")
            
        elif 'news' in query:
            speak(f"Here's a list of the latests news headlines.")
            speak(get_latest_news())
            speak("For your convenience, I am printing it out on your screen.")
            print(*get_latest_news(), sep='\n')
            
        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting a weather report for {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it out on your screen.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
