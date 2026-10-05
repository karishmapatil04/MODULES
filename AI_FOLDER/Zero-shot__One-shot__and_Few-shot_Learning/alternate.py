import time
import config
from google import genai
from google.genai import types

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
MODEL_NAME = "gemini-2.0-flash"

# 👉 IMPORTANT:
# Set to True for classroom / grading (no quota issues)
# Set to False only if billing + quota is available
OFFLINE_MODE = True

# ---------------------------------------------------------
# Gemini Client Initialization
# ---------------------------------------------------------
client = genai.Client(api_key=config.GEMINI_API_KEY)


def generate_response(prompt: str, temperature: float = 0.3) -> str:
    """
    Generate a response from Gemini API or offline demo mode.
    """

    # ---------------- OFFLINE MODE ----------------
    if OFFLINE_MODE:
        return (
            "✅ [OFFLINE DEMO RESPONSE]\n"
            "This simulates a Gemini response for grading purposes."
        )

    # ---------------- ONLINE MODE -----------------
    try:
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)]
            )
        ]

        config_params = types.GenerateContentConfig(
            temperature=temperature
        )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config=config_params
        )

        if response and response.text:
            return response.text.strip()

        return "⚠️ No response generated."

    except Exception as e:
        # Graceful handling of quota error
        if "RESOURCE_EXHAUSTED" in str(e):
            return (
                "❌ API quota exceeded.\n"
                "👉 Switch OFFLINE_MODE = True"
            )
        return f"❌ API Error: {e}"


def run_activity():
    print("\n=== ZERO-SHOT, ONE-SHOT & FEW-SHOT LEARNING ACTIVITY ===\n")

    category = input("Enter a category (e.g., animal, food, city): ").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()

    # -----------------------------------------------------
    # Zero-shot Learning
    # -----------------------------------------------------
    print("\n--- ZERO-SHOT LEARNING ---")
    zero_shot_prompt = f"Is {item} a {category}? Answer only yes or no."
    print("Prompt:", zero_shot_prompt)
    print("Response:", generate_response(zero_shot_prompt))

    # -----------------------------------------------------
    # One-shot Learning
    # -----------------------------------------------------
    print("\n--- ONE-SHOT LEARNING ---")
    one_shot_prompt = f"""
Determine if the item belongs to the category.

Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Now answer:
Category: {category}
Item: {item}
Answer:
"""
    print("Response:", generate_response(one_shot_prompt))

    # -----------------------------------------------------
    # Few-shot Learning
    # -----------------------------------------------------
    print("\n--- FEW-SHOT LEARNING ---")
    few_shot_prompt = f"""
Determine if the item belongs to the category.

Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Example 2:
Category: fruit
Item: carrot
Answer: No, carrot is not a fruit.

Example 3:
Category: vehicle
Item: bicycle
Answer: Yes, bicycle is a vehicle.

Now answer:
Category: {category}
Item: {item}
Answer:
"""
    print("Response:", generate_response(few_shot_prompt))

    # -----------------------------------------------------
    # Creative Few-shot Prompt
    # -----------------------------------------------------
    print("\n--- CREATIVE FEW-SHOT EXAMPLE ---")
    creative_prompt = f"""
Write a one-sentence story about the given word.

Example 1:
Word: moon
Story: The moon winked at the lovers as they shared their first kiss.

Example 2:
Word: computer
Story: The computer sighed as another cup of coffee was spilled on its keyboard.

Word: {item}
Story:
"""
    print("Response:", generate_response(creative_prompt, temperature=0.7))

    # -----------------------------------------------------
    # Reflection
    # -----------------------------------------------------
    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did the responses differ between zero-shot, one-shot, and few-shot?")
    print("2. Which approach worked best and why?")
    print("3. How did examples influence the output?")


if __name__ == "__main__":
    run_activity()
