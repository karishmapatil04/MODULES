import random

# -------------------------------------------------
# Try importing Text-to-Speech library
# -------------------------------------------------
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️  Run: pip install pyttsx3")


# -------------------------------------------------
# Initialize Text-to-Speech
# -------------------------------------------------
def setup_tts():
    """Initialize text-to-speech engine"""
    if not TTS_AVAILABLE:
        return None

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 0.9)

        # Optional: choose voice (0 = male, 1 = female on most systems)
        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[0].id)

        return engine
    except Exception as e:
        print("❌ TTS Error:", e)
        return None


# -------------------------------------------------
# Speak text (with fallback)
# -------------------------------------------------
def speak(engine, text):
    """Speak text or print if audio unavailable"""
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except:
            print(f"🔇 [AUDIO]: {text}")
    else:
        print(f"🔇 [AUDIO]: {text}")


# -------------------------------------------------
# Sample phrases
# -------------------------------------------------
def get_samples():
    return [
        "Hello! I am your computer!",
        "Python is awesome!",
        "This is artificial intelligence speaking!",
        "Welcome to the future!",
        "I can talk using Python!"
    ]


# -------------------------------------------------
# Main program
# -------------------------------------------------
def main():
    print("🤖 AI VOICE LAB")
    print("================")
    print("Type anything and I will speak it!")
    print("Commands: sample | help | exit")

    engine = setup_tts()

    if engine:
        print("✅ Voice engine ready")
    else:
        print("⚠️  Audio not available (text-only mode)")

    speak(engine, "Hello! Type something for me to say!")

    while True:
        text = input("\n🎤 You: ").strip()

        if text.lower() == "exit":
            speak(engine, "Goodbye! See you soon!")
            break

        elif text.lower() == "sample":
            phrase = random.choice(get_samples())
            print(f"🎲 Sample: {phrase}")
            speak(engine, phrase)

        elif text.lower() == "help":
            print("📌 Commands:")
            print("  sample → hear a random phrase")
            print("  exit   → quit the program")
            print("  help   → show commands")

        elif text:
            speak(engine, text)

        else:
            print("💡 Type something, or use 'sample', 'help', or 'exit'")


# -------------------------------------------------
# Safe execution
# -------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Exiting safely. Bye!")
