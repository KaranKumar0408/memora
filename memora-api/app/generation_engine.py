import os
import time
import requests

from dotenv import load_dotenv

load_dotenv(".env")

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_URL = (
    "https://router.huggingface.co/hf-inference/models/"
    "black-forest-labs/FLUX.1-schnell"
)


def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": prompt
    }

    response = requests.post(
        MODEL_URL,
        headers=headers,
        json=payload,
        timeout=180,
    )

    content_type = response.headers.get("content-type", "")

    if response.status_code != 200:
        return {
            "status": "failed",
            "provider": "huggingface",
            "error": response.text,
        }

    if "image" not in content_type:
        return {
            "status": "failed",
            "provider": "huggingface",
            "error": response.text[:500],
            "content_type": content_type,
        }

    filename = f"generated_{int(time.time())}.jpg"
    output_path = os.path.join("uploads", filename)

    with open(output_path, "wb") as f:
        f.write(response.content)

    return {
        "status": "success",
        "provider": "FLUX.1-schnell",
        "image_url": f"http://127.0.0.1:8000/uploads/{filename}",
    }