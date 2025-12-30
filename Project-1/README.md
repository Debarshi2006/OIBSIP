# 🎙️ Python Voice Assistant (OIBSIP Project 1)
A responsive voice assistant built with Python that performs tasks based on voice commands. This project focuses on speech recognition, text-to-speech synchronization, and web automation.

## 🚀 Features

* Voice Recognition:
Converts spoken language into text using the SpeechRecognition library.

* Interactive Responses: 
Greets the user and provides the current system time and date.

* Web Automation: 
Automatically opens a browser to perform Google searches based on user voice queries.

* Hardware Optimized: 
Features a custom initialization loop to prevent audio muting issues on Windows laptops.


* Smart Listening: 
Includes ambient noise adjustment and a calibrated energy threshold for faster response times.
+1

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Debarshi2006/OIBSIP.git]
   cd OIBSIP

2. **Install required libraries:**
    ```bash
    pip install speechrecognition pyttsx3 pyaudio

3. **Run the assistant:**
    ```bash
    python voice_assistant.py

## ⌨️ Usage Commands
* "Hello": The assistant will introduce itself and ask how it can help.

* "Time": Announces the current time in 12-hour format.

* "Date": Announces today's full date (Month, Day, Year).

* "Search": The assistant will ask what to search for, then open your default browser with the results.

* "Exit" / "Stop": Terminating the program gracefully.

## 📁 Project Context
This is Project 1 of the Oasis Infobyte Python Programming Internship. It fulfills all "Beginner" level requirements including speech-to-text, predefined responses, and task execution.