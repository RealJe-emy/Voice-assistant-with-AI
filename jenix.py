import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import openai
import transformers


# OpenAI API Key (replace 'your_openai_api_key' with your actual API key)
openai.api_key = 'Add Your API_KEY'

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female voice, 0 for male


def speak(audio):
    """Text-to-speech output."""
    engine.say(audio)
    engine.runAndWait()


def take_command():
    """Listen for a command and transcribe it."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("User said:", query)
    except Exception as e:
        print(e)
        speak("I didn't understand that.")
        return None
    return query


def open_application(app_name):
    """Open specified application based on recognized name."""
    app_paths = {
        "spotify": "C:\\Users\\YourUsername\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe",
        "atom": "C:\\Users\\jerem\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc",
        "notepad": "notepad.exe",
        # "whatsapp": "",
        # "telegram": "",
        "github": "C:\\Users\\jerem\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc",
        "vmware": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VMware",
        "chrome": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        # "settings": "",
        "brave": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        "anydesk": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\AnyDesk",
        "vs code": "C:\\Users\\jerem\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code",
        "word": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        "access": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        "powerpoint": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        "excel": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        "packet tracer": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Cisco Packet Tracer",
        "edge": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        "localsend": "C:\\Users\\jerem\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs",
        "firefox": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        "falcon": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Falcon C++",
        # "netflix": "",
        # "player": "",
        "pgadmin": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PostgreSQL 17",
        "publisher": "C:\ProgramData\Microsoft\Windows\Start Menu\Programs",





    }
    app_name = app_name.lower()
    if app_name in app_paths:
        os.startfile(app_paths[app_name])
        speak(f"Opening {app_name}")
    else:
        speak(f"Sorry, I don't know how to open {app_name}. Please add it to the app list.")


def ai_response(query):
    """Use OpenAI API to generate a response for more complex or conversational queries."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" or "gpt-4" depending on availability
        messages=[
            {"role": "user", "content": query}
        ],
        max_tokens=100
    )
    return response.choices[0].message['content']

if __name__ == '__main__':
    speak("Jenix activated. How can I help you?")

    while True:
        query = take_command()
        if query:
            query = query.lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            elif 'open' in query:
                app_name = query.replace("open", " ").strip()
                open_application(app_name)
            elif 'play music' in query:
                speak("Playing music on Spotify")
                webbrowser.open("https://open.spotify.com/")
            elif 'exit' in query or 'sleep' in query:
                speak("Goodbye!")
                break
            else:
                # Call AI response for any other type of query
                ai_reply = ai_response(query)
                speak(ai_reply)
