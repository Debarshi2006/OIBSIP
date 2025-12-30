import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

# Initialize the recognizer
recognizer = sr.Recognizer()

def speak(text):
    print(f"Assistant: {text}")
    try:        
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) 
        engine.setProperty('rate', 170)           
        
        engine.say(text)
        engine.runAndWait()
        
        del engine 
    except Exception as e:
        print(f"Speaker Error: {e}")

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        recognizer.pause_threshold = 0.8
        
        print("\nListening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            return command
        except Exception:
            return ""

def respond_to_command(command):
    """Logic for the assistant's features."""
    if not command:
        return

    # Hello Response
    if 'hello' in command:
        speak("Hello! I am up and running. How can I help you today?")

    # Time Feature
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {current_time}")

    # Date Feature
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%B %d, %Y')
        speak(f"Today is {current_date}")

    # Google Search Feature
    elif 'search' in command:
        speak("What would you like me to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Opening Google search results for {query}")
        else:
            speak("I didn't hear a search topic.")

    # Help / Unknown
    else:
        speak("I heard you, but I don't have a command for that yet. Try saying time, date, or search.")

if __name__ == "__main__":
    speak("Voice assistant initialized. How can I assist you?")
    
    while True:
        # Short delay to allow the audio driver to switch from 'Speak' to 'Listen'
        time.sleep(0.5)
        
        user_input = listen()
        
        # Stop condition
        if 'exit' in user_input or 'stop' in user_input or 'goodbye' in user_input:
            speak("Goodbye! Have a great day.")
            break
            
        respond_to_command(user_input)