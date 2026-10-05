import requests

# Correct Hugging Face Sentiment Analysis API URL
api_url = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# Replace with your Hugging Face API token
headers = {
    "Authorization": "Bearer API_KEY_HERE"
}

# Sample text for sentiment analysis
text = "I love this movie! It was fantastic."

# Send POST request to the Hugging Face API
response = requests.post(api_url, headers=headers, json={"inputs": text})

if response.status_code == 200:
    result = response.json()
    # ✅ Fix: Access nested list correctly
    label = result[0][0]['label']
    score = result[0][0]['score']
    print(f"Sentiment: {label} with confidence score: {score:.4f}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
