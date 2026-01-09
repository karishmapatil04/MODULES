import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

recognizer = sr.Recognizer()
translator = Translator()

# ------------------ SPEECH TO TEXT ------------------
def speech_to_text():
    with sr.Microphone() as source:
        print("🎤 Speak in English...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("📝 You said:", text)
        return text
    except:
        print("❌ Could not understand speech")
        return None

# ------------------ TRANSLATE ------------------
def translate_text(text, target_lang):
    translated = translator.translate(text, dest=target_lang)
    print("🌍 Translated:", translated.text)
    return translated.text

# ------------------ SPEAK (REAL VOICE) ------------------
def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# ------------------ LANGUAGE MENU ------------------
def select_language():
    print("\n🌍 Choose language:")
    print("1. Hindi")
    print("2. Marathi")
    print("3. French")
    print("4. Spanish")

    return {
        "1": "hi",
        "2": "mr",
        "3": "fr",
        "4": "es",
    }.get(input("Enter choice: "), "hi")

# ------------------ MAIN ------------------
def main():
    lang = select_language()
    text = speech_to_text()

    if text:
        translated = translate_text(text, lang)
        print("🔊 Speaking...")
        speak(translated, lang)
        print("✅ Done!")

if __name__ == "__main__":
    main()
