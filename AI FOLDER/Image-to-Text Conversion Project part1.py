import requests
import io
from PIL import Image
#from config import HF_API_KEY

def get_caption(image_path):
    url = "https://router.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
    headers = {
        "Authorization": f"Bearer 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"
    }

    # Load image
    image = Image.open(image_path).convert("RGB")
    buf = io.BytesIO()
    image.save(buf, format="JPEG")
    buf.seek(0)

    response = requests.post(url, headers=headers, data=buf.getvalue())

    # 🔍 Debug info
    if response.status_code != 200:
        print("API Error:", response.status_code)
        print("Response text:", response.text)
        return

    try:
        result = response.json()
        print("Caption:", result[0]["generated_text"])
    except Exception as e:
        print("JSON Error:", e)
        print("Raw response:", response.text)

# Run
image_path = r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\AI FOLDER\example.jpg"
print("Generating caption...")
get_caption(image_path)
