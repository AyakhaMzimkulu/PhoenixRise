from cgi import print_environ_usage
from ipaddress import ip_address
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke,get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email
from functions.os_ops import open_calculator, open_camera, open_cmd, open_discord, open_notepad
from pprint import pprint

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        
        if 'open notepad' in query:
            open_notepad()
            
        elif 'open discord' in query:
            open_discord()
            
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
            
        elif 'open camera' in query:
            open_camera()
        
        elif 'open calculator' in query:
            open_calculator()
            
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\nFor your convenience, I am printing it on the screen.')
            print(f'Your IP Address is {ip_address}')
            
        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {reults}")
            speak("For your convenience, I am printing it on the screen.")
            print(results)
            
        elif 'youtube' in query:
            speak('What would you like to play on Yourtube?')
            video = take_user_input().lower()
            play_on_youtube
            
        elif 'search on goolgle' in query or 'google' in query or 'open google' in query:
            speak('What would you like to search?')
            query = take_user_input().lower()
            search_on_google(query)
            
        elif "send email" in query or "email" in query:
            speak("What email address do I send to? Please enter it in the console:")
            reciever_address = input("Enter email address: ")
            speak("What should the subject be?")
            subject = take_user_input().capitalize()
            speak("What is the message?")
            message = take_user_input().capitalize()
            if send_email(reciever_address, subject, message):
                speak("Message sent.")
            else:
                speak('Something went wrong while sending the email. Please check the error logs sir.')
                
        elif 'joke' in query:
            speak(f"Get a load of this, lol")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen.")
            pprint(joke)
            
        elif 'advice' in query:
            speak(f"Someone once said that")
            advice = get_random_advice()
            speak(advice)
            speak("That's quite wise if you ask me, haha")
            
        elif 'news' in query:
            speak(f"Latest news headlines are")
            speak(get_latest_news())
            speak('For your convenince, I am printing it on the screen.')
            print(*get_latest_news(), sep='\n')
            
        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://iapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak(f"For your convenience, I am printing it on the screen.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")