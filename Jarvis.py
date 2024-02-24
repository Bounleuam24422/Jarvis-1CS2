
import speech_recognition as sr
import pyttsx3
from ecapture import ecapture as ec
import wikipedia
import json
import os
import datetime
import webbrowser
import time
import requests


print('Loading your AI personal assistant - Jarvis')


#synthesis and recognition of voice.
engine=pyttsx3.init('sapi5')                       
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('rate',170)

#Convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function: Greet the user according to the time of the computer
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


#function: Record microphone
def takeCommand():
    r=sr.Recognizer()                      #
    with sr.Microphone() as source:        #
        print("Listening...")              # "Listening"
        audio=r.listen(source)             #


#function: Speech Recognition
        try:
            statement=r.recognize_google(audio,language='en-in') #
            print(f"user said:{statement}\n") #

#Case: Do not understand or do not understand clearly
        except Exception as e:
            speak("Pardon me, please say that again") #
            return "None" #No information found # while loop
        return statement

speak("Loading your AI personal assistant Jarvis") #
wishMe() #Take the time from the machine to speak according to the conditions

# conditions: It is a check that the spoken information corresponds to which person
if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?") #Case: while loop
        statement = takeCommand().lower()
        if statement==0:      #If no information is found           
            continue        #while loop
 
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...') #
            statement = statement.replace("wikipedia", "") #
            try:
                results = wikipedia.summary(statement, sentences=3) #Search information in wikipedia
                speak("According to Wikipedia") #
                print(results) #Show alternate results
                speak(results) #Speak according to the results   
                
            except Exception as e: #
                speak(f"no result found for {statement}") 

        # break

        if "stop" in statement or "ok bye" in statement or "good bye" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break
        
        #Conditions: open the program
        elif "open the word" in statement or "open word" in statement:
                speak("Okay sir, Open Word") 
                os.system("start WINWORD.EXE") #
        
        #Conditions: open the web
        elif 'open the map' in statement:
            webbrowser.open_new_tab("https://shorturl.asia/v0wfs") #
            speak("google map is open now") 
            time.sleep(5) #
        
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
       
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.com/news/world")
            speak('Here are some headlines from the Times of BBC,Happy reading')
            time.sleep(5)

        #Conditions: what time?
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") #
            speak(f"the time is {strTime}") #

        #Codditions:Camera
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg") #Capture the image from the camera
        
        #search
        elif 'search'  in statement:
            statement = statement.replace("search", "") #
            webbrowser.open_new_tab(statement) #
            time.sleep(5)

        #Case: Need to close the program system
        elif "close the word" in statement or "close word" in statement:
                speak("Okay sir, closing word") 
                os.system("taskkill /f /im WINWORD.EXE") #
        
        elif "close the edge" in statement or "close edge" in statement:
                speak("Okay sir, closing edge")
                os.system("taskkill /f /im msedge.exe")
        
        #log off
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            os.system("shutdown -l")
        
        

time.sleep(3)












