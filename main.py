import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import psutil

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Speak function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""

# Respond to commands
def process_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif 'open notepad' in command:
        os.system('notepad')
        speak("Opening Notepad")

    elif 'open chrome' in command:
        os.system('start chrome')
        speak("Opening Chrome")

    elif 'search' in command:
        search_term = command.replace('search', '')
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
        speak(f"Searching for {search_term}")

    elif 'battery' in command:
        battery = psutil.sensors_battery()
        speak(f"Battery is at {battery.percent} percent")

    elif 'who is' in command or 'tell me about' in command:
        topic = command.replace('who is', '').replace('tell me about', '').strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except Exception:
            speak("Sorry, I couldn't find that on Wikipedia.")

    elif 'play music' in command:
        music_dir = 'music'  # Path to music folder
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        else:
            speak("No music files found.")

    elif 'exit' in command or 'bye' in command:
        speak("Goodbye! Have a nice day!")
        exit()

    else:
        speak("Sorry, I don't understand that command.")

# Main loop
speak("Hello! I am Jarvis. How can I help you today?")
while True:
    user_command = listen()
    if user_command:
        process_command(user_command)
