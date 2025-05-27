import base64
from openai import OpenAI

api_key = '99e33e32b4a9a6bf2a96a22ed522bb6a' 
base_url = "https://chat-ai.academiccloud.de/v1"
model = "internvl2.5-8b" 

client = OpenAI(
    api_key = '99e33e32b4a9a6bf2a96a22ed522bb6a',
    base_url = "https://chat-ai.academiccloud.de/v1",
)

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "a01-000u.png"

base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model = model,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)
print(response.choices[0])
