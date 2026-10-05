from google import genai
import config

# -----------------------------------------
# Initialize Gemini Client
# -----------------------------------------
try:
    client = genai.Client(api_key=config.GEMINI_API_KEY)
except Exception as e:
    print("❌ Failed to initialize Gemini client:", e)
    client = None  # Proceed with offline mode


# -----------------------------------------
# Get a working model for content generation
# -----------------------------------------
def get_working_model():
    if client is None:
        return None
    try:
        models = client.models.list_models()
        # Find first model that supports generate_content
        for m in models:
            if "generate_content" in m.supported_generation_methods:
                return m.name
        return None
    except Exception as e:
        print("⚠️ Could not list models:", e)
        return None


WORKING_MODEL = get_working_model()
if WORKING_MODEL:
    print(f"✅ Using Gemini model: {WORKING_MODEL}")
else:
    print("⚠️ No compatible Gemini model found. Using offline fallback mode.")


# -----------------------------------------
# Offline fallback responses
# -----------------------------------------
def offline_response(prompt: str) -> str:
    prompt_lower = prompt.lower()
    if "ai" in prompt_lower or "artificial intelligence" in prompt_lower:
        return (
            "Artificial Intelligence (AI) is the field of computer science that "
            "creates systems capable of performing tasks that usually require human intelligence, "
            "like learning, reasoning, and problem-solving."
        )
    elif "python" in prompt_lower:
        return "Python is a popular programming language used for many applications like AI, web development, and automation."
    elif "technology" in prompt_lower:
        return "Technology refers to the tools, machines, and systems created to solve problems and make life easier."
    else:
        return f"Sample response for: '{prompt}'"


# -----------------------------------------
# Generate AI response safely (with fallback)
# -----------------------------------------
def generate_response(prompt: str) -> str:
    if client is None or WORKING_MODEL is None:
        # Offline fallback
        return offline_response(prompt)

    try:
        response = client.models.generate_content(
            model=WORKING_MODEL,
            contents=prompt
        )

        if hasattr(response, "text"):
            return response.text
        elif response.candidates:
            return response.candidates[0].content.parts[0].text
        else:
            return offline_response(prompt)

    except Exception as e:
        error = str(e)
        # Fallback for errors
        return offline_response(prompt)


# -----------------------------------------
# Interactive Prompt Engineering Tutorial
# -----------------------------------------
def silly_prompt():
    print("\n🎯 AI Prompt Engineering Tutorial")
    print("--------------------------------")
    print("Concepts Covered:")
    print("• Clarity & Specificity")
    print("• Contextual Information")
    print("\nLet's start by crafting a vague prompt, making it more specific, and then adding context.")

    # Step 1: Vague Prompt
    vague_prompt = input("\n🟡 STEP 1: Enter a VAGUE prompt: ")
    print("\n🤖 AI Response (Vague Prompt):")
    print("-" * 50)
    print(generate_response(vague_prompt))

    # Step 2: Specific Prompt
    specific_prompt = input("\n🟢 STEP 2: Make it MORE SPECIFIC: ")
    print("\n🤖 AI Response (Specific Prompt):")
    print("-" * 50)
    print(generate_response(specific_prompt))

    # Step 3: Contextual Prompt
    contextual_prompt = input("\n🔵 STEP 3: Add CONTEXT to your prompt: ")
    print("\n🤖 AI Response (Contextual Prompt):")
    print("-" * 50)
    print(generate_response(contextual_prompt))

    # Reflection Questions
    print("\n📘 Reflection Questions")
    print("----------------------")
    print("1. How did the AI's response improve with specificity?")
    print("2. How did context change the depth of the answer?")
    print("3. Which prompt produced the most relevant and tailored response? Why?")


# -----------------------------------------
# Run the tutorial
# -----------------------------------------
if __name__ == "__main__":
    silly_prompt()
