#!/usr/bin/env python3

import os
import base64
from openai import OpenAI

api_key = '99e33e32b4a9a6bf2a96a22ed522bb6a'
base_url = "https://chat-ai.academiccloud.de/v1"
model = "internvl2.5-8b"
image_dir = "./images/data"  
output_file = "saia_handwritten_text.txt"

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def encode_image(image_path):
    """Reads and base64 encodes an image file."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def extract_text_from_image(image_path):
    """Sends image to the LLM and returns extracted handwritten text."""
    b64_image = encode_image(image_path)
    prompt = "Read the handwritten text in this image. Return only the text. Do not explain."
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_image}"}},
                ],
            }
        ],
    )
    return response.choices[0].message.content.strip()

with open(output_file, "w") as out:
    for filename in sorted(os.listdir(image_dir)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(image_dir, filename)
            print(f"[+] Processing {filename}")
            try:
                text = extract_text_from_image(image_path)
                out.write(f"--- {filename} ---\n{text}\n\n")
            except Exception as e:
                out.write(f"--- {filename} ---\nERROR: {str(e)}\n\n")
                print(f"[!] Failed: {filename} – {e}")

