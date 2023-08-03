import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good After Noon!")
    else:
        speak("Good Evening!")
    speak("I am Lady Jarvis. Tell me how can i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}")
    except Exception as e:
        # print(e)

        print("Say It Again Please...")
        return "None"
    return query

if __name__=="__main__":
    speak("Hello Mr. Mirza How Are you")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google...")
            webbrowser.open("google.com")
        elif 'play music' in query:
            speak("Playing Music")
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {strTime}")
        elif 'bye bye' in query:
            speak("Goodbye Mirza! If you have any more tasks in the future, feel free to ask. Have a great day!")
            break 