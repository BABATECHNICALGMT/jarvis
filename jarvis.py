
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and  hour<12:
        speak("good Morning!")

    elif hour>=12 and hour<18:
        speak("good afternone!")

    else:
        speak("good Evening!")

    speak("I am Jarvis Robot please tall me how may I help you")

#it taken microphone input from the user returns starting input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("sorry sir! say that again please...")
        return "none"
    return query



if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=9)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        speak(f"sir, next command!")

    elif 'open google' in query:
        webbrowser.open("google.com")
        speak(f"sir, next command!")

    elif 'play music' in query:
        music_dir = 'E:\\mouve'
        songs = os.listdir(music_dir)
        speak(f"sir, next command")
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
        speak(f"sir, next command")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strtime("%H:%M:%S")
        speak(f"sir, the time is{strTime}")

