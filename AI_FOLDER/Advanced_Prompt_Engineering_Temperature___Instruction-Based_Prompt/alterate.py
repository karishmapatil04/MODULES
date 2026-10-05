import os
import time
import sys
from google import genai
from google.genai import types
import config

# Recommended: pip install google-genai

def wait_with_timer(seconds):
    """Displays a countdown timer in the console."""
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\rCooling down API... {i}s remaining  ")
        sys.stdout.flush()
        time.sleep(1)
    print("\rReady for next request!          ")

def generate_response(prompt, temperature=0.5):
    """Generate a response with automatic retries for rate limits."""
    # Using 1.5-flash for better free-tier stability
    model_id = "gemini-1.5-flash-latest" 
    
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                ),
            )
            return response.text
        except Exception as e:
            if "429" in str(e):
                print(f"\n[Rate Limit Hit] Attempt {attempt+1}/3. Waiting 30 seconds...")
                wait_with_timer(30)
            else:
                return f"Error: {str(e)}"
    return "Max retries reached. Please try again in a few minutes."

def temperature_prompt_activity():
    print("=" * 60)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE EXPLORATION")
    print("=" * 60)
    
    base_prompt = input("\nEnter a creative prompt: ")
    
    # We use a 15-second gap between successful calls to stay under the free limit
    temps = [0.1, 0.5, 0.9]
    labels = ["LOW (Deterministic)", "MEDIUM (Balanced)", "HIGH (Creative)"]
    
    for i in range(3):
        print(f"\n--- {labels[i]} (Temp: {temps[i]}) ---")
        response = generate_response(base_prompt, temperature=temps[i])
        print(response)
        
        if i < 2: # Don't wait after the last one
            wait_with_timer(15)

if __name__ == "__main__":
    temperature_prompt_activity()