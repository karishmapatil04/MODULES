import requests
from PIL import Image
from io import BytesIO

def generate_image(prompt):
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

print("Text to Image — Free & Working (Pollinations AI)")
while True:
    text = input("\nPrompt (or 'exit'): ")
    if text.lower() == "exit":
        break
    
    try:
        img = generate_image(text)
        img.show()
    except Exception as e:
        print("Error:", e)
