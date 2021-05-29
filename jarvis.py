import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """This function will take a string and it will speak it"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """This function will wish you as per the current time"""
    hour = int(datetime.datetime.now().hour)
    if hour>=2 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")

    elif hour>=18 and hour<=21:
        speak("Good evening sir")
    
    else:
        speak("Hi sir")

    speak("How can I help you sir?")


def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        # print("Something went wrong :",e)
        print("Sorry sir, can you repeat once.")
        return "None"

    return query


def sendEmail(reciever, subject):
    """It takes a reciever email and the content of the email and sends a email with that content"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_mail_id','your_mail_id_password')
    server.sendmail('your_mail_id', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    
    while 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipeia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "E:\\Superhit Remixes"
            songs = os.listdir(music_dir)
            songIndex = random.randint(0, len(songs)-1)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[songIndex]))

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Abhik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What you want to write?")
                content = takeCommand()
                to = "your_another_mail_id" #to which you are sending mail
                sendEmail(to, content)
                speak('Email has been sent')

            except Exception as e:
                print(e)
                speak("Sorry sir something went wrong")
        
        elif 'shutdown' in query:
            print("Thanks for your time sir\nShutting down...")
            speak("Thanks for your time sir")
            speak("Shutting down...")
            exit()
        
