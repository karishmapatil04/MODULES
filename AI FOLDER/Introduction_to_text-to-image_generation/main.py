import requests

from PIL import Image

from io import BytesIO


 

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

 

def generate_image_from_text(prompt: str, negative_prompt: str = None) -> Image.Image:

    """

    Sends a text prompt (and optional negative prompt) to the Stable Diffusion API

    and returns the generated image as a Pillow Image.

    """

    headers = {"Authorization": f"Bearer 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"}

 

    # Build payload with optional parameters

    payload = {

        "inputs": prompt,

        # 'options' is a common parameter block used by some Inference Endpoints.

        # Actual support depends on the model endpoint configuration.

        "options": {}

    }

    if negative_prompt:

        # Hypothetical negative prompt handling

        payload["options"]["negative_prompt"] = negative_prompt

    

    try:

        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

        response.raise_for_status()

 

        if 'image' in response.headers.get('Content-Type', ''):

            image = Image.open(BytesIO(response.content))

            return image

        else:

            raise Exception("The response is not an image. Possibly an error message.")

    except requests.exceptions.RequestException as e:

        raise Exception(f"Request failed: {e}")

 

def main():

    print("=== Custom Payload Text-to-Image Generator ===")

    print("Type 'exit' to quit.\n")

 

    while True:

        prompt = input("Enter a text prompt:\n> ").strip()

        if prompt.lower() == "exit":

            print("Goodbye!")

            break

        

        # Ask if the user wants to add a negative prompt

        neg_prompt_input = input("Enter a negative prompt (or press Enter to skip):\n> ").strip()

        negative_prompt = neg_prompt_input if neg_prompt_input else None

 

        print("\nGenerating image with the following parameters:")

        print(f" Prompt: {prompt}")

        if negative_prompt:

            print(f" Negative Prompt: {negative_prompt}")

        else:

            print(" Negative Prompt: (None)")

        print("Please wait...\n")

 

        try:

            image = generate_image_from_text(prompt, negative_prompt=negative_prompt)

            image.show()

 

            save_option = input("Do you want to save this image? (yes/no): ").strip().lower()

            if save_option == "yes":

                file_name = input("Enter a name for the image file (without extension): ").strip() or "generated_image"

                # Basic validation for file name

                file_name = "".join(c for c in file_name if c.isalnum() or c in ('_', '-')).rstrip()

                image.save(f"{file_name}.png")

                print(f"Image saved as {file_name}.png\n")

        except Exception as e:

            print(f"An error occurred: {e}\n")

        

        print("-" * 70 + "\n")

 

if __name__ == "__main__":

    main()