from datetime import datetime
from email.mime import audio
import pyttsx3                         #this library is used for text to speech conversion
import datetime                        #for current time in greetings module
import speech_recognition as sr        #It allows computers to understand human language.
import wikipedia                       #will be used to access different info
import webbrowser                      #in built module
import os                              #to play music
import smtplib


engine=pyttsx3.init('sapi5')           #sapi3 is provided by microsoft it is used to get voices from windows
voices=engine.getProperty('voices')
# print(voices[1].id)                  #it gives the voices present in our system
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()                 #runAndWait(): This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you. engine.


#****************function to greet user*******************
def greetings():
    hour=int(datetime.datetime.now().hour)  #used to get current time
    if hour>=0 and hour<12:
        speak("Good Morning Sir ")
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Pirate , How may i help you ? ")




#******************function to understand language***********************************
def takecommand():
    '''
    it takes command from user usinf different functions like 
    1)sr.recognizer class - helps machine to understand human language
    2)pause_threshhold -pause_threshold seconds of non-speaking or there is no more audio input. The ending silence is not included.
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:  # source of the microphone(speaking)
        print('Listning......')      # it will be diplayed on the screen to let user know that machine is listning
        r.energy_threshold=800       # minimum audio energy to consider for recording
        r.pause_threshold=0.8          # it will wait for 0.8 sec when there is no sound , we can increase the time from 1 to 2,3,4 depending upon the pace of the user
        audio=r.listen(source)       # listen -Records a single phrase from ``source`` (an ``AudioSource`` instance) into an ``AudioData`` instance, which it returns
    try:
        print('Recognizing.....')
        query=r.recognize_google(audio,language='en-in')
        print('User said = ',query)   
    except Exception as e:
        # print(e)                   # we will comment it out as we dont want to see errors in the console

        speak('Sorry ! can you say that again please....')
        return 'None'

    return query



#*****************for security reasons we will not run the followinf************************8
def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()                                    #command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.
    server.starttls()                                #Puts the connection to the SMTP server into TLS mode
    server.login("shubhamyourmail@gmail.com","your pass")  
    server.sendmail("shubhamyourmail@gmail.com",to,content)
    server.close()



if __name__ == "__main__":
    speak("Hello , SSKO")
    greetings()
    while True:
        query=takecommand().lower()
        #Logic to execute task starts from here
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia", '')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open whatsapp web' in query:
            webbrowser.open("whatsapp.com")
        elif 'open chrome' in query:
            webbrowser.open("chrome.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        
        elif 'play music' in query:
            music_dir='D:\\Videos\\audio'                     #double slash is used to escape the sequece
            songs=os.listdir(music_dir)                       #all songs will be stored into the list
            print(songs)
            os.startfile(os.path.join(music_dir,songs[16])) 

        elif "what time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        elif "open code" in query:
            c_path="C:\\Users\\rahul\\Desktop\\ssko\\Microsoft VS Code\\Code.exe"
            os.startfile(c_path)
        elif "open my documents" in query:
            s_path="C:\\Users\\rahul\\OneDrive\\Desktop\\ssko"
            os.startfile(s_path)
        elif "for interview" in query:
            s_path="C:\\Users\\rahul\\OneDrive\\Desktop\\ssko\\for interview"
            os.startfile(s_path)
        
        #********************for security reasons we will not run the following****************
        elif "send email to shubham" in query:
            try:
                speak("What should i say")
                content=takecommand()
                to="shubhamyourmail@gmail.com"
                sendemail(to,content)
                speak("your email has sent")
            except Exception as e:
                print(e)

                print("Sorry ! something went wrong")
        
        elif "wish" in query:
            speak("Wishing you a very happy wala birthday Arnav ,stay blessed")
            exit()
        
        elif "how are you" in query:
            speak("I am fine , sir")
            
        
        elif "thanks for your help bye" in query:
            speak("your most welcome , have a good day")
            exit()