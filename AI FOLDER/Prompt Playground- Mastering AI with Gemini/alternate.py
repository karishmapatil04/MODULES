from openai import OpenAI
import config


# -----------------------------------------
# Initialize OpenAI Client
# -----------------------------------------
try:
    client = OpenAI(api_key=config.OPENAI_API_KEY)
except Exception as e:
    print("❌ Failed to initialize OpenAI client:", e)
    exit()


# -----------------------------------------
# Generate AI response safely
# -----------------------------------------
def generate_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error: {e}"


# -----------------------------------------
# Interactive Prompt Engineering Tutorial
# -----------------------------------------
def silly_prompt():
    print("\n🎯 AI Prompt Engineering Tutorial")
    print("--------------------------------")
    print("Concepts Covered:")
    print("• Clarity & Specificity")
    print("• Contextual Information")

    print("\n🟡 STEP 1: Enter a VAGUE prompt")
    vague_prompt = input("> ")
    print("\n🤖 AI Response (Vague Prompt):")
    print("-" * 40)
    print(generate_response(vague_prompt))

    print("\n🟢 STEP 2: Make the prompt MORE SPECIFIC")
    specific_prompt = input("> ")
    print("\n🤖 AI Response (Specific Prompt):")
    print("-" * 40)
    print(generate_response(specific_prompt))

    print("\n🔵 STEP 3: Add CONTEXT")
    contextual_prompt = input("> ")
    print("\n🤖 AI Response (Contextual Prompt):")
    print("-" * 40)
    print(generate_response(contextual_prompt))

    print("\n📘 Reflection Questions")
    print("----------------------")
    print("1. How did the response improve with specificity?")
    print("2. How did context change the depth of the answer?")
    print("3. Which prompt worked best and why?")


# -----------------------------------------
# Run Program
# -----------------------------------------
if __name__ == "__main__":
    silly_prompt()
