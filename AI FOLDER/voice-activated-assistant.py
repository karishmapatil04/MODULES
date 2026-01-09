import speech_recognition as sr
import pyttsx3
from datetime import datetime
import random

# -------------------------------
# GLOBAL SETTINGS
# -------------------------------
VOICE_INDEX = 1   # 0 = male, 1 = female
SPEECH_RATE = 150
user_name = ""

# -------------------------------
# TEXT TO SPEECH
# -------------------------------
def speak(text):
    print("🤖 Assistant:", text)
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[VOICE_INDEX].id)
    engine.setProperty("rate", SPEECH_RATE)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# -------------------------------
# SPEECH INPUT
# -------------------------------
def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"✅ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("There was a network issue.")

    return ""

# -------------------------------
# COMMAND HANDLER
# -------------------------------
def respond_to_command(command):
    global user_name, VOICE_INDEX

    if "hello" in command:
        speak(f"Hi {user_name}!" if user_name else "Hello! How can I help you?")

    elif "your name" in command:
        speak("I am your smart Python assistant.")

    elif "time" in command:
        speak(f"The time is {datetime.now().strftime('%H:%M')}")

    elif "date" in command:
        speak(f"Today is {datetime.now().strftime('%B %d, %Y')}")

    elif "my name is" in command:
        user_name = command.replace("my name is", "").strip().capitalize()
        speak(f"Nice to meet you, {user_name}!")

    elif "fact" in command:
        speak(random.choice([
            "Honey never spoils.",
            "Octopuses have three hearts.",
            "Bananas are berries.",
            "The Eiffel Tower grows in summer.",
            "Water can boil and freeze at the same time."
        ]))
    
    #elif "use male voice" in command:
    #    VOICE_INDEX = 0
    #   speak("Switched to male voice.")

    #elif "use female voice" in command:
    #    VOICE_INDEX = 1
    #    speak("Switched to female voice.")
    

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I'm not sure how to help with that.")

    return True

# -------------------------------
# MAIN LOOP
# -------------------------------
def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()
