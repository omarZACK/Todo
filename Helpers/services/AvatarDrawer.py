from PIL import Image, ImageDraw, ImageFont
import os
from django.utils import timezone


def generate_profile_image(letter, email):
    img = Image.new('RGB', (100, 100), color=(103, 206, 212))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arialbd.ttf", 50)
    bbox = d.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((100 - text_width) / 2, (80 - text_height) / 2)
    d.text(position, letter, fill=(240, 240, 240), font=font)
    date_path = timezone.now().strftime('%Y/%m/%d')
    dir_path = os.path.join('media', 'profile_picture', date_path)
    os.makedirs(dir_path, exist_ok=True)
    filename = f"{email.lower().replace(' ', '_')}.png"
    image_path = os.path.join(dir_path, filename)
    img.save(image_path)

    return image_path
