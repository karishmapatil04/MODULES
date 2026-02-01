import streamlit as st
import re
from PIL import Image
from io import BytesIO
import base64
from openai import OpenAI
from config import OPENAI_API_KEY   # store your API key here


# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def is_prompt_safe(prompt: str) -> bool:
    """
    Basic filter to avoid generating harmful or restricted content.
    """
    forbidden_keywords = [
        "violence", "weapon", "gun", "blood", "nude", "porn", "drugs", "hate", "racism", "sex",
        "terror", "bomb", "abuse", "kill", "death", "suicide", "self-harm", "hate speech"
    ]
    pattern = re.compile("|".join(forbidden_keywords), re.IGNORECASE)
    return not bool(pattern.search(prompt))


def generate_image(prompt: str):
    """
    Generate an image using OpenAI Images API.
    Returns PIL image or error message.
    """
    if not is_prompt_safe(prompt):
        return None, "⚠️ Your prompt contains restricted or unsafe content. Please modify and try again."

    try:
        response = client.images.generate(
            model="gpt-image-1",   # OpenAI image model
            prompt=prompt,
            size="1024x1024"
        )

        # OpenAI returns base64 image data
        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        image = Image.open(BytesIO(image_bytes))
        return image, None

    except Exception as e:
        return None, f"Error during image generation: {str(e)}"


def main():
    st.set_page_config(page_title="Safe AI Image Generator", layout="centered")
    st.title("🖼️ Safe AI Image Generator (OpenAI)")

    st.write(
        "Enter a description to generate a safe AI image using OpenAI. "
        "Examples: 'A serene sunset over a mountain lake', 'A futuristic city skyline at night'"
    )

    st.info("This app uses OpenAI GPT Image model for image generation.")

    with st.form(key="image_gen_form"):
        prompt = st.text_area(
            "Image Description:",
            height=120,
            placeholder="Describe the image you want to generate..."
        )
        submit = st.form_submit_button("Generate Image")

        if submit:
            if not prompt.strip():
                st.warning("⚠️ Please enter an image description.")
            else:
                with st.spinner("Generating image... Please wait..."):
                    image, error = generate_image(prompt.strip())

                if error:
                    st.error(error)
                elif image:
                    st.image(image, caption="Generated Image", use_container_width=True)
                    st.session_state.generated_image = image
                else:
                    st.error("Failed to generate image. Try a different prompt.")

    # Download button
    if hasattr(st.session_state, 'generated_image') and st.session_state.generated_image:
        buf = BytesIO()
        st.session_state.generated_image.save(buf, format='PNG')
        byte_im = buf.getvalue()

        st.download_button(
            label="⬇️ Download Generated Image",
            data=byte_im,
            file_name="ai_generated_image.png",
            mime="image/png",
            help="Click to download the generated image"
        )


if __name__ == "__main__":
    main()
