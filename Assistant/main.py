import speech_recognition as sr
import pyttsx3 as pyt
import pywhatkit 

listener = sr.Recognizer()
engine = pyt.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try :
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()   # * converting spoken text to lower case
            if 'alexa' in command :
                command = command.replace('alexa','')
                talk(command)
                print(command)
    except :
        pass
    return command
    

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command :
        song = command.replace('play','') 
        talk('playing ' + song)
        pywhatkit.playonyt(song)    # * this will play song on youtube



run_alexa()