import os
import time
import requests
from config import HF_API_KEY


def main():
    """
    Prompts the user for an images folder, processes each image in that folder
    using the Hugging Face API for captioning, and saves results to a summary file.
    """

    # -----------------------------
    # 1. Prompt user for folder path
    # -----------------------------
    folder_path = input("Enter the path to your images folder (press Enter for default): ").strip()

    if not folder_path:
        folder_path = r"C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\AI FOLDER\AI-Powered_Image_Descriptions"

    if not os.path.isdir(folder_path):
        print(f"❌ Folder '{folder_path}' does not exist. Exiting.")
        return

    # -----------------------------
    # 2. Hugging Face API details
    # -----------------------------
    MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    # -----------------------------
    # 3. Process all images
    # -----------------------------
    image_files = [f for f in os.listdir(folder_path)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print(f"❌ No valid image files found in '{folder_path}'. Exiting.")
        return

    captions = []

    for img_name in image_files:
        img_path = os.path.join(folder_path, img_name)
        print(f"\n🖼 Processing: {img_path}")

        try:
            with open(img_path, "rb") as img_file:
                image_bytes = img_file.read()
        except Exception as e:
            print(f"❌ Could not load image '{img_name}'. Error: {e}")
            continue

        # -----------------------------
        # API request with error handling
        # -----------------------------
        for attempt in range(3):  # retry if the model is loading
            try:
                response = requests.post(API_URL, headers=headers, data=image_bytes)
                try:
                    result = response.json()
                except ValueError:
                    print(f"⚠ JSON decode error. Raw response: {response.text}")
                    result = {"error": "Invalid JSON received"}
                break
            except requests.exceptions.RequestException as req_e:
                print(f"⚠ Network error while processing '{img_name}': {req_e}")
                continue

        # -----------------------------
        # Handle HF "loading" case
        # -----------------------------
        if isinstance(result, dict) and "error" in result:
            if "currently loading" in result["error"].lower():
                print("⏳ Model is loading... waiting 8 seconds")
                time.sleep(8)
                continue  # retry image
            else:
                print(f"❌ API Error: {result['error']}")
                continue

        # -----------------------------
        # Extract caption
        # -----------------------------
        try:
            caption = result[0]["generated_text"]
        except Exception:
            caption = "No caption found."

        print(f"✅ Caption: {caption}")
        captions.append((img_name, caption))

    # -----------------------------
    # 4. Save results
    # -----------------------------
    if captions:
        summary_file = os.path.join(folder_path, "captions_summary.txt")
        with open(summary_file, "w", encoding="utf-8") as sf:
            for img_name, caption in captions:
                sf.write(f"{img_name}: {caption}\n")

        print(f"\n📄 All captions saved to: {summary_file}")
    else:
        print("\n❌ No captions were generated.")


if __name__ == "__main__":
    main()
