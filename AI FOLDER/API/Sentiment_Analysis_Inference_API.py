'''
*FIRST WORKING CODE*

from huggingface_hub import InferenceClient

client = InferenceClient(api_key="API_KEY_PASTE_HERE")

text = "I love Python!"
result = client.text_classification(text=text)

# Pretty print
top = max(result, key=lambda x: x.score)
print(f"Sentiment: {top.label} ({top.score:.2%} confidence)")'''

'''
*SECOND WORKING CODE*
from huggingface_hub import InferenceClient

HF_API_KEY = "API_KEY_PASTE_HERE"

# ✅ New-style client (auto routes via latest inference API)
client = InferenceClient(api_key=HF_API_KEY)

text = "I love learning about AI! It's so fascinating."

# ✅ This works with latest hub (no 404s)
result = client.text_classification(
    text,
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# ✅ Pretty output
for r in result:
    print(f"{r.label}: {r.score:.4f}")'''


import requests

def classify_text(text):
    HF_API_KEY = ""
    # Correct endpoint (no router)
    API_URL = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)

    #print("Status Code:", response.status_code)
    #print("Response Text:", response.text)

    if response.status_code == 200:
        return response.json()
    else:
        print("Request failed")
        return None

if __name__ == "__main__":
    sample_text = "I love using Hugging Face APIs!"
    result = classify_text(sample_text)
    print(result)


