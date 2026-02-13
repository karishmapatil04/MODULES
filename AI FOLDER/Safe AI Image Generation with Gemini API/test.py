from openai import OpenAI
import base64
from PIL import Image
from io import BytesIO

client = OpenAI(api_key="IzaSyAIOgoffkPD71siMob-oZ1MPmlCBH45uZc")

response = client.images.generate(
    model="gpt-image-1",
    prompt="A futuristic city with flying cars",
    size="1024x1024"
)

img_base64 = response.data[0].b64_json
img_bytes = base64.b64decode(img_base64)

image = Image.open(BytesIO(img_bytes))
image.show()
