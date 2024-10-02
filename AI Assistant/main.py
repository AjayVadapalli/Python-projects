import speech_recognition as sr
import pyttsx3
import webbrowser
import playlist

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in c.lower():
        webbrowser.open("https://google.com/")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=playlist.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak(" Hello, I am AI Assistant! I am here to help you")
    while True:
        r=sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Say something...")
                audio = recognizer.listen(source,timeout=2,phrase_time_limit=1)
            text = recognizer.recognize_google(audio)
            print("You said: ", text)
            if(text.lower() == "hello"):
                speak("Yep!")
                with sr.Microphone() as source:
                    print("Zoro Active...")  
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
                    
        except Exception as e:
            print("Error: ", format(e))
            
