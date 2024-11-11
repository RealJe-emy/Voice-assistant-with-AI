import pyttsx3
import speech_recognition as sr
from transformers import pipeline

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize Hugging Face model for text generation (GPT-2)
generator = pipeline('text-generation', model='gpt2')

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, the service is down.")
            return None

# Function to process user query and get AI response
def ai_response(query):
    if query:
        response = generator(query, max_length=50)[0]['generated_text']
        return response
    else:
        return "I couldn't understand your request."

# Main function to run the assistant
def run_assistant():
    speak("Hello, I'm your voice assistant. How can I help you today?")
    while True:
        query = listen()
        if query:
            ai_reply = ai_response(query)
            print(f"AI: {ai_reply}")
            speak(ai_reply)
        else:
            break

# Run the assistant
if __name__ == "__main__":
    run_assistant()
