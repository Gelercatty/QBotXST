import io
from pprint import pprint
from PIL import Image
from requests import post

# Preprocess the image as per Fluffle its documentation
image = Image.open("01.jpg")
width, height = image.size


def calculate_size(width, height, target):
    def calculate_size(d1, d2, d1_target): return round(d1_target / d1 * d2)

    if width > height:
        return calculate_size(height, width, target), target

    return target, calculate_size(width, height, target)


image.thumbnail(calculate_size(width, height, 256))
buffer = io.BytesIO()
image.save(buffer, "png")

# And then reverse search the preprocessed image
headers = {
    "User-Agent": "furBot/1.0 (by Gelercat on Twitter)"
}
files = {
    "file": buffer.getvalue()
}
data = {
    "platforms": [
        "Twitter", 
        # "e621",
    ],
    "limit": 8
}

response = post("https://api.fluffle.xyz/v1/search", headers=headers, files=files, data=data).json()
pprint(response)