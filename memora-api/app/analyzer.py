from PIL import Image
import numpy as np


def extract_dominant_color(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((100, 100))

    pixels = np.array(image).reshape(-1, 3)

    average_color = pixels.mean(axis=0)

    r, g, b = average_color.astype(int)

    return {
        "rgb": [int(r), int(g), int(b)],
        "label": f"rgb({int(r)}, {int(g)}, {int(b)})"
    }