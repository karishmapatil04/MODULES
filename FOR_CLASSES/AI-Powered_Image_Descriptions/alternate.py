import requests
from config import HF_API_KEY

API_URL = "https://router.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

image_source = r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\FOR_CLASSES\AI-Powered_Image_Descriptions\test.jpg"

with open(image_source, "rb") as f:
    files = {"file": f}
    response = requests.post(API_URL, headers=headers, files=files)

print("Status code:", response.status_code)
print("Response text:", response.text[:500])  # first 500 chars

if response.status_code == 200:
    try:
        result = response.json()
        caption = result[0].get("generated_text", "No caption found.")
        print("Caption:", caption)
    except Exception as e:
        print("Failed to parse JSON:", e)
