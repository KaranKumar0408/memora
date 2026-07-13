from PIL import Image
import numpy as np


def calculate_similarity(image_a, image_b):

    img1 = Image.open(image_a)
    img2 = Image.open(image_b)

    img1 = img1.resize((100, 100))
    img2 = img2.resize((100, 100))

    arr1 = np.array(img1).astype(np.float32)
    arr2 = np.array(img2).astype(np.float32)

    difference = np.mean(np.abs(arr1 - arr2))

    color_score = max(0, 100 - (difference / 255) * 100)

    return {
        "identity": round(color_score),
        "style": round(color_score),
        "color": round(color_score),
        "overall": round(color_score),
    }