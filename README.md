Voice Assistant with AI Integration
#JENIX
This is a voice-controlled assistant that can perform tasks like opening applications, searching Wikipedia, playing music, and providing conversational AI responses. It integrates OpenAI's GPT-3 for dynamic responses and handles a variety of commands.

Features
Text-to-Speech (TTS): The assistant can speak back responses using the pyttsx3 library.
Speech Recognition: The assistant listens for commands using the SpeechRecognition library.
Wikipedia Search: Allows the assistant to search Wikipedia and provide a summary.
Application Launcher: The assistant can open a variety of applications like Spotify, Chrome, Notepad, etc.
AI Integration: Uses OpenAI’s GPT-3 for more complex or conversational queries.
Play Music: Opens Spotify to play music.
Friendly Commands: Includes commands like "buy me tea" for fun interactions.

libraries to install:
pip install pyttsx3 speechrecognition wikipedia openai
Make sure you have Chrome and Spotify installed or add paths for other apps.

Replace the API key placeholder with your actual OpenAI API key:

python
Copy code
openai.api_key = 'your_openai_api_key'
Usage
Run the assistant script:

bash
Copy code
python assistant.py
You can interact with the assistant by saying commands like:

"Open Spotify"
"Search Wikipedia for Python programming"
"Play music"
"What is the weather today?" (AI-powered response)
"Buy me tea" (Just for fun!)
Commands
Functional Commands
Open Applications: "Open Spotify", "Open Chrome", "Open Notepad"
Wikipedia Search: "Search Wikipedia for Python"
Play Music: "Play music", "Play on Spotify"
Exit: "Exit", "Sleep"
Fun Command (AI-powered)
"Buy me tea": A fun, conversational response from the AI.
AI Integration
This assistant uses OpenAI’s GPT-3 to handle dynamic and conversational queries. You can interact with it for more general conversations or queries like:

"Tell me a joke"
"What’s the capital of France?"
"Explain quantum physics"
The assistant will generate an answer using AI.

How It Works
The assistant listens to your command via the microphone.
It processes the voice input and recognizes commands.
If the command is a predefined action (like opening an app), it performs the action.
If the command requires a conversational response, it queries the AI (OpenAI GPT-3) and provides the response.
You can exit the assistant anytime by saying "exit" or "sleep".
License
This project is open-source and free to use. Feel free to modify and extend the assistant as per your needs!
